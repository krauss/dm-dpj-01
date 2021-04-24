import urllib
import time
from bs4 import BeautifulSoup

    
HEADERS = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-GPC": "1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_ip_info(ip):
    """Given a string that starts with:  IPDecode("%3c%61%20%68%72%65%66%3d..."),
    this function decodes it to a human-readable format
    """
    soup = None
    if ip:
        ip = ip.lstrip('IPDecode').strip('(")')
        soup = BeautifulSoup(urllib.parse.unquote(ip), 'html.parser').text

    return soup

def timestamp_decorator(func):
    """Decorator that stamps the time a function takes to execute."""
    def wrapper(*args, **kwargs):
        start = time.time()

        func(*args, **kwargs)        

        end = time.time()
        print(f'Finished in {end-start:.3} secs')
    return wrapper