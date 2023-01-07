import requests
from bs4 import BeautifulSoup
import urllib.request
import requests
from requests_html import HTMLSession
import time

class HTTPService:
    '''
    New and fast http service to make requests to google
    '''
    def __init__(self):
        self.session = HTMLSession()
        self.ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"

    def make_req(self, query):
        result = self.session.get(f"https://www.google.com/search?q={query}$cr=countryEN&num=40")
        return result.text

def req_via_proxy(query, proxy, country_search_code="EN", res_number=40):
    proxies = {'http': proxy, 'https': proxy} 
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    print(requests.get("https://ident.me", proxies=proxies).text)
    req = requests.get(f"http://www.google.com/search?q={query}&cr=country{country_search_code}&num={res_number}", headers={'User-agent': ua}, proxies=proxies)
    return req.text

    


def make_req_requests(query, country_search_code, res_number):
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    req = requests.get(f"http://www.google.com/search?q={query}&cr=country{country_search_code}&num={res_number}", headers={'User-agent': ua})
    return req.text

def parser(data):
    soup = BeautifulSoup(data, "html.parser")
    result_blocks = soup.find_all(
        'div', attrs={'class': 'g'})
    all_links = []
    for div in result_blocks:
        link = div.find('a', href=True)
        title = div.find('h3')
        descr_div = div.select('div[data-content-feature]')
        description = "Not parsed"
        if len(descr_div) > 0:
            description = descr_div[0].find_all('span')
            description_buff = []
            for span in description:
                description_buff.append(str(span.contents[0]))
            description = ''.join(description_buff)
        if (link and title):
            all_links.append((link['href'], title.contents[0], description))
    return all_links


def make_request(query, proxy="nn", country_search_code="EN", res_number=100):
    proxy_support = urllib.request.ProxyHandler({'http' : 'http://130.185.119.20:3128'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    with urllib.request.urlopen(f"http://www.google.com/search?q={query}&cr=country{country_search_code}&num={res_number}") as response:
        res = response.read()
        with open("a.html", "wb") as file:
            file.write(res)
        return res

def search(query, country_search_code="EN", res_number=20, mode="pure", http_service=None):
    if mode == "pure":
        cont = make_req_requests(query, country_search_code, res_number)
    elif mode == "proxy":
        cont = req_via_proxy(query=query, proxy="http://68.183.191.179:44290")
    elif mode == "new": # For tests BETA
        cont = http_service.make_req(query)

    return parser(cont)

def search_via_spr(query: str, spr_server: str, country_search_code: str = "EN", res_number: int = 40):
    data = requests.get(f"{spr_server}/search?query={query}").json()
    return parser(data["data"])
    


if __name__ == "__main__":
    print("[DEBUG] Native request")
    time_start = time.time()
    res = search(query="Null pointer exception c++", mode="pure")
    spent = time.time() - time_start
    print(f"[DEBUG] Time spent: {spent}; About {1 / spent} RPS")
    print(res)
    http = HTTPService()
    time_start = time.time()
    search("null pointer", http_service=http)
    spent = time.time() - time_start
    print(f"[DEBUG] Time spent: {spent}; About {1 / spent} RPS")