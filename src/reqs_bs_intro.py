import requests
from bs4 import BeautifulSoup as BS

r = requests.get('http://poincare.matf.bg.ac.rs/~nemanja_micovic/rs.html')
r.encoding = 'utf-8'
soup = BS(r.text, 'html.parser')

#hvatamo tag kome je id news
obavestenja = soup.find(id='news')

#hvatamo prvo obavestenje iz liste obavestenja
obavestenje = obavestenja.find_next('ul').find_next('li')

print(obavestenje.text)

#print(soup.prettify())



