import requests
from bs4 import BeautifulSoup
import urllib.request
import requests

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
        if (link and title):
            all_links.append((link['href'], title.contents[0]))
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

def search(query, country_search_code="EN", res_number=20):
    cont = make_req_requests(query, country_search_code, res_number)
    return parser(cont)


if __name__ == "__main__":
    res = search("Null pointer exception c++")
    print(res)
