import cgitb
import time
from flask import Flask
import requests
import json
from bs4 import BeautifulSoup

# start_response('200 OK', [('Content-Type', 'text/html')])
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

app = Flask(__name__)
# @app.route('/')
# location=input("Enter a location: ") # add eventually: get input from javascript
def yelp_restaurants():
    restaurant_list=[]
    item_start_number = 0
    for i in range(10):
        URL = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Indianapolis&start=' + str(item_start_number*10)
        page = requests.get(URL,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        for item in soup.select('[class*=container]'):
            try:
                if(item.find('h4')):
                    # filters out sponsored restaurants
                    name = item.find('h4').get_text()            
                    if(name[0].isnumeric()):
                        rating = soup.select('[aria-label*=rating]')[0]['aria-label']
                        food_type = item.select('div div div div div div div div div span span span a')[0].get_text()
                        address = item.select('div div div div div div div div div div p span')[0].get_text()
                        restaurant = {
                            'name': name[name.find('\xa0')+1:],
                            'food_type': food_type,
                            'rating': rating,
                            'address': address
                            }
                        restaurant_list.append(restaurant)
            except Exception as e:
                raise e
                print('Error, restaurant not found!')
        item_start_number+=1
    return restaurant_list

# def save(restaurant_list):
#     with open('restaurants.txt', 'w') as outfile:
#         json.dump(restaurant_list, outfile)

# print(yelp_restaurants())