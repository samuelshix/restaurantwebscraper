import cgitb
import time
import requests
from bs4 import BeautifulSoup

start_response('200 OK', [('Content-Type', 'text/html')])
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# location=input("Enter a location: ") # add eventually: get input from javascript
item_start_number = 0
for i in range(10):
    URL = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Indianapolis&start=' + str(item_start_number*10)
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    for item in soup.select('[class*=container]'):
        try:
            if(item.find('h4')):
                # filters out sponsored restaurants
                name = item.find('h4').get_text()            
                if(name[0].isnumeric()):
                    rating = soup.select('[aria-label*=rating]')[0]['aria-label']
                    food_type = item.select('div div div div div div div div div span span span a')[0].get_text()
                    print(name)
                    print(rating)
                    print(food_type)
                    print('*********************')
                
        except Exception as e:
            raise e
            print('')
    item_start_number+=1

# print(soup.prettify())
# results = soup.find_all('span', class_=' raw__09f24__3Obuy')

# print(results.prettify())
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