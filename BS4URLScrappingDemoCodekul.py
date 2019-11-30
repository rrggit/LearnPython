#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "http://www.codekul.com"

req = requests.get(url, headers)

soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())