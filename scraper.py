import urllib.request
from bs4 import BeautifulSoup

target = "https://www.reddit.com/top"
# download the URL and extract the content inot the variable html
request = urllib.request.Request(target)
html = urllib.request.urlopen(request).read()

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parer')
#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div",attrs={'id':'siteTable'})
#Now we go into main_table and get every a element in it which has a class "title" 
links = main_table.find_all("a",class_="title")

#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted 
#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted 
extracted_records = []
for link in links: 
    title = link.text
    url = link['href']
    #There are better ways to check if a URL is absolute in Python. For sake simplicity we'll just stick to .startwith method of a string 
    # https://stackoverflow.com/questions/8357098/how-can-i-check-if-a-url-is-absolute-using-python 
    if not url.startswith('http'):
        url = "https://reddit.com"+url 
    # You can join urls better using urlparse library of python. 
    # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin 
    record = {
        'title':title,
        'url':url
        }
    extracted_records.append(record)
print(extracted_records)