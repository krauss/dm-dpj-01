import time
import click
import os
import csv
from questionary import questionary, Choice
from .proxy import Proxy
from bs4 import BeautifulSoup
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession

#---------------------------------- Web Scrapping function
def scrapper(proxyq):    
    start_time = time.time()

    print(f'\nFetching proxy data...')

    with FuturesSession(max_workers=7) as session:
        futures = [session.get(f'http://www.freeproxylists.net/?page={page}') for page in range(2, 3)]

        for req in as_completed(futures):
            if req.result().status_code == 200:
                prox_soup = BeautifulSoup(bytes(req.result().content), features="lxml")
                proxyq.append(Proxy(prox_soup))


    stop_time = time.time()
    print(f'Fetching finished in {stop_time-start_time:.3} sec')

#---------------------------------- Game processing function
def dumper(proxyq):
    start_time = time.time()

    for game in proxyq:
        try:
            with open(os.path.join(os.getcwd(), 'export', f'proxy_list.json'), 'w', encoding='utf-8') as json_file:
                json_file.write(game.get_game_json())
        except OSError as err:
            print(f'Error: permission error {os.strerror(err.errno)}, stack_trace: {err.with_traceback()}')

        print(f"File ./export/{game}.json saved!")
    

    stop_time = time.time()
    print(f'Saving finished in {stop_time-start_time:.3} sec')

#---------------------------------- 
proxy_queue = []

#---------------------------------- Main method
#@click.command()
def main():
    """Proxy Scrapper - CLI"""
    print("+", "-" * 30, "+")
    print("|", " " * 30, "|")
    print("|", "Proxy Scrapper - CLI".center(30), "|")
    print("|", " " * 30, "|")
    print("+", "-" * 30, "+\n")
    
    scrapper(proxy_queue, competition, str(division).lower(), season, sample, file_format)
    dumper(proxy_queue, competition, str(division).lower(), season, sample, file_format)

#---------------------------------- Entry point
if __name__ == '__main__':
    main()