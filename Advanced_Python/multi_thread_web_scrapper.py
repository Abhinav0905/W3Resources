import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import urllib.robotparser
from urllib.parse import urlparse, urljoin

class ScrapeWeb:

    def __init__(self, baseurl):
        self.parsed_url = urlparse(baseurl)
        self.base_url = baseurl
        self.robots_url = urljoin(baseurl, '/robots.txt')

    def is_allowed(self, url):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(self.robots_url)
        rp.read()
        return rp.can_fetch("*", url)

    def fetch_page(self, urlparse):
        if not self.is_allowed(urlparse):
            print(f"Paring is not allowed{urlparse}")
            return None
        
        try:
            response = requests.get(urlparse)
            if response.status_code == 200:
                print(f"successfully fetched {urlparse}")
                soup = BeautifulSoup(response.content, 'html.parser')
                return soup
            else:
                print(f"failed to extract url form the website{urlparse}")


        except Exception as e:
            print(f"catching the exceptation here {str(e)},{response.status_code}")
            raise
        return None
    
    def extract_link(self, soup, base_url):
        links = []
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            links.append(full_url)
        return links

    def scrape_urls(self,urls,max_worker=5):
        with ThreadPoolExecutor(max_worker=max_worker) as executor:
            features = {executor.submit(self.fetch_page,url): url for url in urls}
            results = []
            for feature in features:
                result = features.result()
                if result:
                    results.append(result)
            return result
        
def main():
    start_url = 'https://example.com'  # Replace with the URL you want to start scraping from
    obj = ScrapeWeb(start_url)
    soup = obj.fetch_page(start_url)
    if not soup:
        return
    
    # Extract links from the start page
    links = obj.extract_links(soup, start_url)
    # Scrape the extracted links
    pages = obj.scrape_urls(links)
    
    # Optionally, you can further process the scraped pages
    for page in pages:
        # Example: print the title of each page
        if page:
            title = page.find('title').get_text()
            print(f'Page title: {title}')

if __name__ == '__main__':
    main()
