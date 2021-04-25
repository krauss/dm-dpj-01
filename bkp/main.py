import time
import os
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get("https://webcache.googleusercontent.com/search?q=cache:https://www.freeproxylists.net/")

#Home page
print('Fetching data for Home page')

keys = {0: 'ip', 1: 'porta', 2: 'protocolo', 4: 'pais', 7: 'uptime'}

proxy_entries = driver.find_element_by_class_name('DataGrid').find_elements_by_tag_name('tr')
for entry in proxy_entries:
    proxy = {}
    for index, column in enumerate(entry.find_elements_by_tag_name('td')):
        if index == 0:
            print(f'Col 0: {column.is_displayed()}')
        if index in (0, 1, 2, 4, 7):
            proxy[keys[index]] = column.text
        
    print(proxy)

    #pages_tag = driver.find_element_by_class_name('page').find_elements_by_tag_name('a')
    #for page in pages_tag:
    #    if page.text == str(page_index):
    #        page.click()
    #        break
    #print(f'Fecthing data for page {page_index}')
    #time.sleep(3)

# Page 2
#print('Fecthing page 2')
#proxy_entries = response.find_element_by_class_name('DataGrid').find_elements_by_tag_name('tr')
#for columns in proxy_entries:
#    print(columns.text)

driver.close()