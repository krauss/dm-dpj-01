import json
import re
from utils import get_ip_info
from bs4 import Tag

#-------------------------------------------------------------------------
#           ProxyList class
#-------------------------------------------------------------------------
class ProxyList:

    def __init__(self):
        self._proxy_list = []

    def add_proxy_list(self, soup):
        '''Method gets a soup as argument and returns an array of dict'''   
        data_grid = soup.find('table', class_='DataGrid')

        if data_grid:
            for line in data_grid.findAll('tr', class_=re.compile('Odd|Even')):
                values = line.findAll('td')        
                if len(values) > 1:
                    self.proxy_list.append(Proxy(values).get_proxy_dict()) 

    #-------------------------------------------------------------------------
    @property
    def proxy_list(self):
        return self._proxy_list

    #-------------------------------------------------------------------------
    @property
    def size(self):
        return len(self._proxy_list)

    #-------------------------------------------------------------------------
    def get_proxy_list_json(self, order_key):
        '''Return a list of proxy object as a JSON order by the order_key param''' 

        if order_key != 'original':
            if order_key == 'uptime':
                self.proxy_list.sort(key=lambda x: x[order_key], reverse=True)
                
            else:
                self.proxy_list.sort(key=lambda x: x[order_key])

        return json.dumps(self.proxy_list, ensure_ascii=False, indent=4)
        

#-------------------------------------------------------------------------
#           Proxy class
#-------------------------------------------------------------------------
class Proxy:

    def __init__(self, soup):
        self._initialize(soup)

    #-------------------------------------------------------------------------
    def _initialize(self, soup):
        '''Method gets a soup as argument and returns an array of dict'''
        
        for index, col in enumerate(soup):
            if index == 0:
                self.ip = get_ip_info(col.contents[0].string)
            elif index == 1:                
                self.porta = (col.text).strip()
            elif index == 2:
                self.protocolo = (col.text).strip()
            elif index == 4:
                self.pais = (col.text).strip()
            elif index == 7:
                self.uptime = (col.text).strip()

    #-------------------------------------------------------------------------
    def get_proxy_dict(self):
        '''Return the proxy object as a dict'''
        return self.__dict__

    #-------------------------------------------------------------------------
    def __str__(self):
        return f"proxy_{self.ip}_{self.porta}"

    #-------------------------------------------------------------------------
    def __repr__(self):
        return r"proxy_" + repr(self.ip+"_"+self.porta)