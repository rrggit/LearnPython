import requests
from bs4 import BeautifulSoup

url = input("Enter a website to extract the URLs from: ")

r  = requests.get("http://" +url)

data = r.text

# Parse HTML and save to BeautifulSoup objects
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

for link in soup.find_all('a.m-r-10='):
    print(link.get('href'))