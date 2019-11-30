from bs4 import BeautifulSoup # python3 -m pip install bs4
import requests # pip3 install requests
import shutil
import html5lib #pip install html5lib
from threading import Thread

url = "http://www.codekul.com"

r = (request.get(url) #save response of server in "r"

try:	
    response = requests.get(url)
except Exception as e:
    print(repr(e))

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify()) 

urlTags = soup.find_all("url")

links = []

for url in urlTags:
    link = url + "/" + tag.get('src')
    links.append(link)

print(links)

def downloadImage(imgUrl, imageName):
    response = requests.get(imgUrl, stream=True)
    with open('images/'+imageName, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

threadList = []

for link in links:
    print(link)
    t1 = Thread(target=downloadImage, args=(link, link.split("/")[-1]))
    t1.start()