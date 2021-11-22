import re
from typing import Union, List
from pathlib import Path
import time
import random
import csv

import requests
from bs4 import BeautifulSoup


def _match_price(string: str) -> str:
    price_pattern = r'[\s]?₱[\s]?\d{,3}(,\d{3})*.\d{2}?'
    try:
        return re.sub(
            r'[^\d.]',
            '',
            re.match(price_pattern, string).group().strip()
        )
    except AttributeError:
        pass


def _eval_price(price: str) -> Union[float, None]:
    try:
        return eval(price)
    except TypeError:
        pass


def _remove_na(old_list: list) -> list:
    return list(filter(None, old_list))


def clean_price(prices: list) -> List[float]:
    return _remove_na(
        [
            _eval_price(
                _match_price(price.decode_contents()))
                    for price in prices
        ]
    )


def export_list(iterable: list, filename: str = 'data.csv') -> None:
    data_path = lambda filename: Path.joinpath(Path.cwd(), 'data', filename)

    with open(data_path(filename), 'w') as f:
        write = csv.writer(f)
        write.writerow(iterable)


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    n_pages = 6
    all_prices = list()

    for page_num in range(1, n_pages + 1):
        URL = f'https://iprice.ph/hp/computing/accessories/chargers/?page={page_num}&so=8'
        response = requests.get(URL, headers=headers)
        page = BeautifulSoup(response.text, 'html.parser')
        prices = clean_price(page.select('div[class="a-"]'))
        all_prices.append(prices)
        print(f"DONE: {page_num}.")
        time.sleep(random.randint(2, 10))

    export_list(all_prices)
