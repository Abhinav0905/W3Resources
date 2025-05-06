class MultiLineHereDocument():
    
    def print_doc_string(self):
        return (""" This is a sample document """)
    
if __name__ == "__main__":
    obj = MultiLineHereDocument()
    abc = obj.print_doc_string()
    print(abc)