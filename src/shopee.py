import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    n_pages = 100
    all_prices = list()

    # for page_num in range(n_pages):
        # page number starts at 0
    URL = f'https://shopee.ph/search?category=11021121&keyword=hp%20charger&page={0}&sortBy=relevancy&subcategory=11021134'
    response = requests.get(URL, headers=headers)
    page = BeautifulSoup(response.text, 'html.parser')
    # prices = page.select('div[class="zp9xm9 xSxKlK _1heB4J"]')
    # prices = page.select('span[class="_1d9_77"]')
        # all_prices.append(prices)
        # print(f"DONE: {page_num}.")
        # time.sleep(random.randint(2, 10))


    print(page)

    # export_list(all_prices)


    # print(prices)
    # <span class="_22f2FV">₱</span><span class="_1d9_77">325</span>
    # <div class="zp9xm9 xSxKlK _1heB4J"><span class="_22f2FV">₱</span><span class="_1d9_77">325</span></div>
