import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://connect.garmin.com/modern/weight"
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')
print(soup)