import time
import os
import requests
import random
from .proxy import Proxy, ProxyList
from .utils import timestamp_decorator, HEADERS
from bs4 import BeautifulSoup


def exporter(proxy_list):
    try:
        with open(os.path.join(os.getcwd(), 'export', f'proxies.json'), 'w', encoding='utf-8') as json_file:
            json_file.write(proxy_list.get_proxy_list_json())
    except OSError as err:
        print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')

    print(f"File proxies.json created in ./export/\n")


@timestamp_decorator
def scrapper(proxy_list):

    for page in range(1, 8):
        print(f'\nFetching page {page}')
        if page == 1:
            req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/', headers=HEADERS)

        else:
            req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/?page={page}', headers=HEADERS)

        if req.status_code == 200:
            prx_soup = BeautifulSoup(bytes(req.content), features="html.parser")
            proxy_list.add_proxy_list(prx_soup)
        
        browsing_time = random.randint(4, 10)
        print(f'Browsing page {page} for {browsing_time} secs')
        time.sleep(browsing_time)
        
    print(f'\nProxies downloaded: {proxy_list.size}')


def main():
    print(" +", "-" * 30, "+")
    print(" |", " " * 30, "|")
    print(" |", "Proxy Scrapper - CLI".center(30), "|")
    print(" |", " " * 30, "|")
    print(" +", "-" * 30, "+\n")
    print(' This CLI application scraps the site\n',
        'below and generates a json file containing\n',
        'one object per proxy entry.\n')
    print(' -> https://www.freeproxylists.net/\n')
    input(' Hit enter to start scrapping: ')
    prx_lst = ProxyList()
    scrapper(prx_lst)
    exporter(prx_lst)


#-------- Entry point
if __name__ == '__main__':
    main()