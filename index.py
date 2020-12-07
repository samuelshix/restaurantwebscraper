from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

URL = 'https://www.yelp.com/search'
location='?find_loc=' + input("Enter a location: ") # get input from javascript
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
results = soup.find_all('span', class_=' raw__09f24__3Obuy')
print(results)
# biztitle = results.find_all('a',class_=' link__09f24__1kwXV link-color--inherit__09f24__3PYlA link-size--inherit__09f24__2Uj95')
# print(results)
# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')
# job_elems = results.find_all('section', class_='card-content')
# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)