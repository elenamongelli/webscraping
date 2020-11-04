from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#Testing with one webpage
my_url = 'https://www.bbc.com/news/world-europe-49345912'

#opening the connection and downloading the page
uClient = uReq(my_url)

#storing the html and closing the connection
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#grabbing text
containers = page_soup.findAll("div", {"class":"css-83cqas-RichTextContainer e5tfeyi2"})

for container in containers:
    paragraph = container.text.strip()
    print (paragraph)


