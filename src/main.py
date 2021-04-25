#!/usr/bin/env python

# main.py

import time
import os
import requests
import random
from questionary import questionary, Choice
from proxy import Proxy, ProxyList
from utils import timestamp_decorator, HEADERS, PROXY_IP_POOL
from bs4 import BeautifulSoup


def exporter(proxy_list, order_key):
    try:
        with open(os.path.join(os.getcwd(), 'export', f'proxies.json'), 'w', encoding='utf-8') as json_file:
            json_file.write(proxy_list.get_proxy_list_json(order_key))
    except OSError as err:
        print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')

    print(f"File proxies.json created in {os.path.join(os.getcwd())}/export \n")


@timestamp_decorator
def scrapper(proxy_list, google_cache):

    for page in range(1, 8):
        print(f'\nFetching page {page}')
        try:
            if page == 1:
                if google_cache:
                    req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/', headers=HEADERS)
                else:
                    proxy = PROXY_IP_POOL[random.randint(0, 165)]
                    req = requests.get(f'https://www.freeproxylists.net/', headers=HEADERS, proxies=proxy)
                    time.sleep(random.randint(3, 9))
            else:
                if google_cache:
                    req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/?page={page}', headers=HEADERS)
                else:
                    proxy = PROXY_IP_POOL[random.randint(0, 165)]
                    req = requests.get(f'https://www.freeproxylists.net/?page={page}', headers=HEADERS, proxies=proxy)
                    time.sleep(random.randint(3, 9))
                
        except ConnectionAbortedError:
            print('Error: connection aborted')
        except ConnectionRefusedError:
            print('Error: connection refused')
        except ConnectionResetError:
            print('Error: connection reset')
        except ConnectionError as conerr:
            print('Error: connection error', conerr)
        else:
            if req.status_code == 200:
                prx_soup = BeautifulSoup(bytes(req.content), features="html.parser")
                proxy_list.add_proxy_list(prx_soup)
        
    print(f'\nProxies downloaded: {proxy_list.size}')

order_key_list = [Choice('original'), Choice('país', value='pais'), Choice('uptime')]

def main():
    print(" +", "-" * 30, "+")
    print(" |", " " * 30, "|")
    print(" |", "Proxy Scrapper - CLI".center(30), "|")
    print(" |", " " * 30, "|")
    print(" +", "-" * 30, "+\n")
    print(' This CLI application scraps the web site\n',
        'below and generates a json file containing\n',
        'a list of proxy object.\n')
    print(' -> https://www.freeproxylists.net/\n')

    google_cache = questionary.confirm(" Do you want to scrap from Google cached pages?").ask()
    order_result = questionary.select(" Select the proxies' order key", choices=order_key_list).ask()
    input('\n Hit enter to start scrapping: ')
    prx_lst = ProxyList()
    scrapper(prx_lst, google_cache)
    exporter(prx_lst, order_result)

#-------- Entry point
if __name__ == '__main__':
    main()