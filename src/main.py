#!/usr/bin/env python

# main.py

import time
import os
import requests
import random
from questionary import questionary, Choice
from proxy import Proxy, ProxyList
from utils import timestamp_decorator, HEADERS
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def exporter(proxy_list, order_key):
    try:
        with open(os.path.join(os.getcwd(), 'export', f'proxies.json'), 'w', encoding='utf-8') as json_file:
            json_file.write(proxy_list.get_proxy_list_json(order_key))
    except OSError as err:
        print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')

    print(f"File proxies.json created in {os.path.join(os.getcwd())}/export \n")


@timestamp_decorator
def scrap_from_cache(proxy_list):  
    print('\nWe aware that when fetching from Google cache, you might get stalled data.\n')  
    for page in range(1, 8):
        print(f'\nFetching page {page}')
        try:
            if page == 1:
                req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/', headers=HEADERS)                
            else:
                req = requests.get(f'http://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/?page={page}', headers=HEADERS)                                                    
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
                prx_soup = BeautifulSoup(bytes(req.content), features="lxml")
                proxy_list.add_proxy_list(prx_soup)
        
    print(f'\nProxies downloaded: {proxy_list.size}')


@timestamp_decorator
def scrap_from_original(proxy_list):

    options = webdriver.firefox.options.Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        try:
            driver.get("https://www.freeproxylists.net/")
        except Exception as ex:
            print('Error: connection error ', ex)        
        print(f'Fecthing data for home page...')

        prx_soup = BeautifulSoup(driver.page_source, features="lxml")
        proxy_list.add_proxy_list(prx_soup)

        for page_index in range(2, 8):
            pages_link_list = driver.find_element_by_class_name('page').find_elements_by_tag_name('a')
            for page_tag in pages_link_list:
                if page_tag.text == str(page_index):
                    try:
                        page_tag.click() # Click the next page <a> tag
                        break
                    except Exception as ex:
                        print('Warning: tiny problem occured when clicking on the page element')    
            driver.implicitly_wait(10)
            print(f'Fecthing data for page {page_index}...')
            prx_soup = BeautifulSoup(driver.page_source, features="lxml")
            proxy_list.add_proxy_list(prx_soup)

    print(f'\nProxies downloaded: {proxy_list.size}')
    

order_key_list = [
    Choice('original'), 
    Choice('país', value='pais'), 
    Choice('uptime'),
    Choice('ip')
]


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

    if google_cache:
        scrap_from_cache(prx_lst)
    else:
        scrap_from_original(prx_lst)

    exporter(prx_lst, order_result)

#-------- Entry point
if __name__ == '__main__':
    main()