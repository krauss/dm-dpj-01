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

PROXY_IP_POOL = [
    {'http':'http://136.243.211.104:80'}, 
    {'http':'http://91.132.139.178:3128'}, 
    {'http':'http://118.179.223.130:80'}, 
    {'http':'http://118.140.160.84:80'}, 
    {'http':'http://90.83.154.85:8080'}, 
    {'http':'http://36.89.8.235:8080'}, 
    {'http':'http://78.47.16.54:80'}, 
    {'http':'http://47.91.153.45:80'}, 
    {'http':'http://47.91.153.45:80'}, 
    {'http':'http://47.91.153.45:80'}, 
    {'http':'http://20.195.17.90:3128'}, 
    {'http':'http://86.123.166.109:8080'}, 
    {'http':'http://218.253.39.60:8380'}, 
    {'http':'http://217.216.36.65:80'}, 
    {'http':'http://218.253.39.60:80'}, 
    {'http':'http://138.199.30.137:3128'}, 
    {'http':'http://201.91.82.155:3128'}, 
    {'http':'http://119.206.79.20:80'}, 
    {'http':'http://62.83.122.160:80'}, 
    {'http':'http://58.152.94.85:8081'}, 
    {'http':'http://218.253.39.60:8197'}, 
    {'http':'http://167.172.191.249:34425'}, 
    {'http':'http://167.172.171.151:36331'},
    {'http':'http://167.172.171.151:40339'},
    {'http':'http://47.57.188.208:80'},
    {'http':'http://47.57.188.208:80'},
    {'http':'http://70.169.141.35:3128'},
    {'http':'http://188.137.48.210:80'},
    {'http':'http://88.255.102.228:8080'},
    {'http':'http://54.36.15.34:3128'},
    {'http':'http://157.230.103.189:38938'},
    {'http':'http://36.90.148.22:3127'},
    {'http':'http://106.51.252.225:80'},
    {'http':'http://188.166.152.26:8080'},
    {'http':'http://167.172.180.40:37885'},
    {'http':'http://167.172.171.151:36127'},
    {'http':'http://175.141.69.200:80'},
    {'http':'http://175.141.69.200:80'},
    {'http':'http://197.248.30.123:80'},
    {'http':'http://197.248.30.123:80'},
    {'http':'http://165.22.64.68:35031'},
    {'http':'http://58.176.147.14:8197'},
    {'http':'http://51.159.24.172:3154'},
    {'http':'http://51.159.24.172:3156'},
    {'http':'http://192.109.165.95:80'},
    {'http':'http://51.159.24.172:3166'},
    {'http':'http://51.159.24.172:3167'},
    {'http':'http://36.82.106.238:8080'},
    {'http':'http://192.109.165.164:80'},
    {'http':'http://58.176.147.14:80'},
    {'http':'http://167.172.180.46:41202'},
    {'http':'http://51.159.24.172:3155'},
    {'http':'http://193.149.225.190:80'},
    {'http':'http://167.172.191.249:44654'},
    {'http':'http://193.149.225.190:80'},
    {'http':'http://178.128.125.16:32990'},
    {'http':'http://192.109.165.129:80'},
    {'http':'http://178.128.143.54:8080'},
    {'http':'http://157.230.41.179:80'},
    {'http':'http://193.149.225.141:80'},
    {'http':'http://14.139.175.194:80'},
    {'http':'http://74.205.128.201:80'},
    {'http':'http://74.205.128.201:80'},
    {'http':'http://137.74.112.21:80'},
    {'http':'http://113.252.245.122:80'},
    {'http':'http://92.204.129.161:80'},
    {'http':'http://194.67.78.220:80'},
    {'http':'http://157.90.4.18:8118'},
    {'http':'http://144.76.241.110:80'},
    {'http':'http://13.127.229.55:80'},
    {'http':'http://167.172.180.46:37121'},
    {'http':'http://135.125.107.126:80'},
    {'http':'http://117.212.192.212:8080'},
    {'http':'http://117.212.192.212:8080'},
    {'http':'http://132.148.85.91:80'},
    {'http':'http://81.173.204.98:80'},
    {'http':'http://91.77.162.117:8080'},
    {'http':'http://81.173.204.98:80'},
    {'http':'http://35.220.171.251:3128'},
    {'http':'http://178.128.24.186:3128'},
    {'http':'http://74.143.245.221:80'},
    {'http':'http://138.201.118.227:80'},
    {'http':'http://47.254.90.125:81'},
    {'http':'http://47.88.7.18:8088'},
    {'http':'http://192.109.165.221:80'},
    {'http':'http://139.59.51.139:80'},
    {'http':'http://192.109.165.246:80'},
    {'http':'http://124.158.167.173:8080'},
    {'http':'http://124.158.167.173:8080'},
    {'http':'http://41.238.115.218:8080'},
    {'http':'http://152.228.163.151:80'},
    {'http':'http://116.80.41.12:80'},
    {'http':'http://95.0.219.204:8080'},
    {'http':'http://192.109.165.135:80'},
    {'http':'http://193.149.225.94:80'},
    {'http':'http://119.110.75.30:63123'},
    {'http':'http://189.146.109.172:80'},
    {'http':'http://210.127.209.150:80'},
    {'http':'http://118.173.232.5:34413'},
    {'http':'http://192.109.165.187:80'},
    {'http':'http://1.4.198.117:80'},
    {'http':'http://192.109.165.98:80'},
    {'http':'http://52.185.204.154:80'},
    {'http':'http://192.109.165.32:80'},
    {'http':'http://173.82.193.91:3128'},
    {'http':'http://49.12.74.188:11626'},
    {'http':'http://63.250.44.215:80'},
    {'http':'http://119.110.66.82:63123'},
    {'http':'http://186.103.203.203:999'},
    {'http':'http://168.138.250.242:80'},
    {'http':'http://186.103.203.203:999'},
    {'http':'http://46.175.70.69:44239'},
    {'http':'http://190.121.131.10:8080'},
    {'http':'http://202.5.56.33:63141'},
    {'http':'http://187.44.1.167:8080'},
    {'http':'http://192.109.165.34:80'},
    {'http':'http://212.33.205.18:8080'},
    {'http':'http://36.89.156.149:8181'},
    {'http':'http://192.109.165.145:80'},
    {'http':'http://180.149.232.149:8080'},
    {'http':'http://190.211.44.164:8080'},
    {'http':'http://91.217.202.174:8080'},
    {'http':'http://12.229.217.226:55443'},
    {'http':'http://136.228.131.67:8080'},
    {'http':'http://186.237.106.20:80'},
    {'http':'http://190.61.46.166:8080'},
    {'http':'http://49.0.93.59:8080'},
    {'http':'http://202.29.6.226:80'},
    {'http':'http://89.20.135.204:80'},
    {'http':'http://27.131.179.197:10443'},
    {'http':'http://159.192.130.233:8080'},
    {'http':'http://194.67.34.84:80'},
    {'http':'http://12.41.126.196:3128'},
    {'http':'http://159.69.38.145:3128'},
    {'http':'http://193.149.225.73:80'},
    {'http':'http://41.60.216.56:23500'},
    {'http':'http://95.216.194.46:1080'},
    {'http':'http://193.122.144.192:80'},
    {'http':'http://219.92.41.106:8080'},
    {'http':'http://36.89.252.155:8080'},
    {'http':'http://110.78.28.94:8080'},
    {'http':'http://12.41.126.196:3128'},
    {'http':'http://157.90.230.151:25105'},
    {'http':'http://181.13.239.13:50002'},
    {'http':'http://190.2.214.92:999'},
    {'http':'http://117.103.5.186:44825'},
    {'http':'http://200.60.124.109:8080'},
    {'http':'http://93.117.72.27:43631'},
    {'http':'http://85.133.210.42:3128'},
    {'http':'http://12.41.126.197:3128'},
    {'http':'http://189.52.154.213:3128'},
    {'http':'http://190.253.241.1:8082'},
    {'http':'http://46.16.78.185:80'},
    {'http':'http://160.202.40.20:55655'},
    {'http':'http://61.19.151.170:8080'},
    {'http':'http://62.99.178.46:37699'},
    {'http':'http://46.35.248.160:55443'},
    {'http':'http://94.28.35.7:8080'},
    {'http':'http://91.185.222.11:80'},
    {'http':'http://158.101.19.129:80'},
    {'http':'http://159.192.147.186:8080'},
    {'http':'http://95.143.220.5:45939'},
    {'http':'http://88.85.97.150:3150'},
    {'http':'http://88.198.82.12:8118'},
    {'http':'http://212.73.73.234:8081'}
]