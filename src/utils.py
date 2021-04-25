import urllib
import time
import platform
from bs4 import BeautifulSoup

    
LINUX = {
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

WINDOWS = {
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

# Define different headers for different platforms
if platform.system() == 'Linux':
    HEADERS = LINUX

elif platform.system() == 'Windows':
    HEADERS = WINDOWS


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