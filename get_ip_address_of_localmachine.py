import socket

def get_ip_address():
    local_hostname = socket.gethostname()
    ip_address = socket.gethostbyname_ex(local_hostname)

    # filtered_ip = [ip for ip in ip_address if not ip.startswith("127.")]

    # first_ip = filtered_ip[:1]

    return ip_address

if __name__ == "__main__":
    result = get_ip_address()
    print (result)