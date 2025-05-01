import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://isubtitles.org"

async def search_sub(query):
    r = requests.get(f"{BASE_URL}/search?kwd={query}").text
    soup1 = bs(r, "lxml")
    all = soup1.find_all("div", class_="row")
    index = []
    title = []
    keys = []
    soup2 = bs(str(all), 'lxml')
    head = soup2.find_all("h3")
    soup3 = bs(str(head), "lxml")
    links = soup3.find_all("a")
    i = 0
    for a in links:
        key = a.get("href").split("/")
        if key[1] not in keys:
            i += 1
            index.append(i)
            title.append(a.text)
            keys.append(key[1])
    return index, title, keys

def get_lang(lang):
    url = f"{BASE_URL}/{lang}"
    r = requests.get(url).text
    soup4 = bs(r, "lxml")
    file = soup4.find_all("table")
    soup5 = bs(str(file), "lxml")
    soup_t = soup5.find_all("a")
    language = []
    index = []
    link = []
    i = 0
    for b in soup_t:
        if b["href"].startswith("/download/"):
            i += 1
            h = b.get("href").split("/")
            btn = h[3]
            if btn not in language:
                index.append(i)
                language.append(btn)
                link.append(f"{BASE_URL}{b.get('href')}")
    return index, language, link
