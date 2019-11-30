import requests
from bs4 import BeautifulSoup

url = "www.codekul.com"

def scrape(url):
    """Scrape scheduled link previews."""
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    r = requests.get(url)
    raw_html = r.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    links = soup.select('body p > a')
    previews = []
    for link in links:
        url = link.get('href')
        r2 = requests.get(url, headers=headers)
        link_html = r2.content
        embedded_link = BeautifulSoup(link_html, 'html.parser')
        link_preview_dict = {
            'title': getTitle(embedded_link),
            'description': getDescription(embedded_link),
            'image': getImage(embedded_link),
            'sitename': getSiteName(embedded_link, url),
            'url': url
            }
        previews.append(link_preview_dict)
        print(link_preview_dict)