import json
from utils import decode_ipaddress
from bs4 import Tag

class Proxy:

    def __init__(self, soup):
        self._proxy_lsit = self._extract_proxy_list(soup)

    #-------------------------------------------------------------------------
    def _extract_proxy_list(self, soup):
        '''Method gets a soup as argument and returns an array of dict'''
        keys = {0: 'ip', 1: 'porta', 2: 'protocolo', 4: 'pais', 7: 'uptime'}

        data_grid = soup.find('table', class_='DataGrid').findAll('tr')

        return [{keys[index]: (col.text if index != 0 else col.contents[0])for index, col in enumerate(line.findAll('td')) if index in (0,1,2,4,7)} for line in data_grid]

    #-------------------------------------------------------------------------
    @property
    def proxy_list(self):
        return self._proxy_lsit

    #-------------------------------------------------------------------------
    def get_proxy_json(self):
        '''Return a list of proxy object as a JSON'''

        return json.dumps(self.proxy_list, ensure_ascii=False, indent=4)

    #-------------------------------------------------------------------------
    def __str__(self):
        return f"game_{self.competition_header['game']}"

    #-------------------------------------------------------------------------
    def __repr__(self):
        return r"game_" + str(self.competition_header['game'])