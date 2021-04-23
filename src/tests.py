import requests
from proxy import Proxy
from bs4 import BeautifulSoup

def main():
    req = requests.get('http://webcache.googleusercontent.com/search?q=cache:http://www.freeproxylists.net/?page=2')

    if req.status_code == 200:
        prox_soup = BeautifulSoup(bytes(req.content), features="html.parser")
        p = Proxy(prox_soup)
        print(p.proxy_list)

if __name__ == '__main__':
    main()