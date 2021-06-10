#!/usr/bin/env python

# main.py

import os
from datetime import datetime
from questionary import questionary, Choice
from proxy import ProxyList
from utils import timestamp_decorator, HEADERS
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException


def exporter(proxy_list, sorting_key, file_format):

    if file_format == 'json':
        try:
            with open(os.path.join(os.getcwd(), 'export', 'data.json'), 'w', encoding='utf-8') as json_file:
                json_file.write(proxy_list.get_proxy_list_json(sorting_key))
        except OSError as err:
            print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')
    else:
        try:
            proxy_list.get_proxy_list_xml(sorting_key).write(
                                                os.path.join(os.getcwd(), 'export', 'data.xml'), 
                                                encoding='utf-8', 
                                                method='xml', 
                                                xml_declaration=True)
        except OSError as err:
            print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')

    print(f" File data.{file_format} created in {os.path.join(os.getcwd())}/export \n")


@timestamp_decorator
def scrap_from_original(proxy_list):

    options = webdriver.firefox.options.Options()
    options.headless = True
    options.page_load_strategy = 'normal'
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("javascript.enabled", True)
    options.profile = firefox_profile
    
    with webdriver.Firefox(options=options) as driver:
        try:
            driver.get("https://www.freeproxylists.net/")
        except Exception as ex:
            print('Error: connection error ', ex)  
        else:
            
            print(f"\n Page: {driver.find_element_by_class_name('current').text}")
            prx_soup = BeautifulSoup(driver.page_source, features="lxml")
            proxy_list.add_proxy_list(prx_soup)

            #try:
            #    
            #    next_page = driver.find_element_by_class_name('page').find_element_by_link_text('Next »')
            #    webdriver.ActionChains(driver).move_to_element(next_page).perform()                
            #    webdriver.ActionChains(driver).context_click(next_page).perform()
            #    #driver.implicitly_wait(5)
            #    WebDriverWait(driver, timeout=3).until(lambda doc: doc.find_element_by_class_name("Caption"))

            #except ElementClickInterceptedException:
            #    print(f' Error: {datetime.now().ctime()}')

            #except NoSuchElementException:
            #    print(' Could not find the Next button.')

            #else:
            #    print(f" Page: {driver.find_element_by_class_name('current').text}")
            #    prx_soup = BeautifulSoup(driver.page_source, features="lxml")
            #    proxy_list.add_proxy_list(prx_soup)

            print(f'\n Proxies downloaded: {proxy_list.size}')

sorting_key_list = [
    Choice('original order', value='original'), 
    Choice('country', value='country'), 
    Choice('uptime'),
    Choice('ip')
]

file_format_list = [
    Choice('json'),
    Choice('xml')
]

def main():
    print(" +", "-" * 30, "+")
    print(" |", " " * 30, "|")
    print(" |", "Proxy Scrapper - CLI".center(30), "|")
    print(" |", " " * 30, "|")
    print(" +", "-" * 30, "+\n")
    print(' This application extracts information\n',
        'from the web site below and generates a JSON\n',
        'file containing a list of proxy objects.\n')
    print(' -> https://www.freeproxylists.net/\n')

    sort_result = questionary.select(" Select the sorting key", choices=sorting_key_list).ask()
    file_format = questionary.select(" Select the file format", choices=file_format_list).ask()
    input('\n Hit enter to start scrapping: ')
    
    prx_lst = ProxyList()
    scrap_from_original(prx_lst)
    exporter(prx_lst, sort_result, file_format)

#-------- Entry point
if __name__ == '__main__':
    main()