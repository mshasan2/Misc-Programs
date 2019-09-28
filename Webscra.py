import requests #pip install requests
import urllib.request #standard module
import time
from bs4 import BeautifulSoup #pip install bs4

url='http://web.mta.info/developers/turnstile.html'#link

response = requests.get(url) #connecting to URL

soup= BeautifulSoup(response.text,"html.parser") #using BeautifulSoup to parse HTML and save to Beautiful soup object

for i in range(36,len(soup.findAll('a'))+1):
    #.findAll to locate <a> tags- hyperlink tags
    #soup.findAll('a')
    #extracting the actual link we want present in line 36
    one_a_tag = soup.findAll('a')[36]
    link= one_a_tag['href']

    download_url='http://web.mta.info/developers/'+link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])

    #to pause, not to spam website with requests
    #avoid being flagged as spammer
    time.sleep(1)
