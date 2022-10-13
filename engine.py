import requests
from bs4 import BeautifulSoup


def search(query, country_search_code="EN", res_number=100):
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    data = requests.get(f"https://www.google.com/search?q={query}&cr=country{country_search_code}&num={res_number}",
                        headers={"User-Agent": user_agent}).text
    soup = BeautifulSoup(data, "html.parser")
    result_blocks = soup.find_all(
        'div', attrs={'class': 'g'})

    all_links = []
    for div in result_blocks:
        link = div.find('a', href=True)
        title = div.find('h3')
        if (link and title):
            all_links.append(link['href'])
    return all_links


if __name__ == "__main__":
    res = search("Issue with sending POST requests using the library requests")
    print(res)
    