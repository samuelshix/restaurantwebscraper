import cgitb
import time
import requests
import json
from bs4 import BeautifulSoup

start_response = ('200 OK', [('Content-Type', 'text/html')])
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# location=input("Enter a location: ") # add eventually: get input from javascript
def yelp_restaurants():
    restaurant_list=[]
    item_start_number = 0
    for i in range(1):
        URL = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Indianapolis&start=' + str(item_start_number*10)
        page = requests.get(URL,headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        restaurants = soup.select('[class*=container]')
        for item in restaurants:
            try:
                if(item.find('h4')):
                    # filters out sponsored restaurants
                    name = item.find('h4').get_text()            
                    if(name[0].isnumeric()):
                        rating = soup.select('[aria-label*=rating]')[0]['aria-label']
                        food_type = item.select('div div div div div div div div div span span span a')[0].get_text()
                        restaurant = {
                            'name': name[name.find('\xa0')+1:],
                            'food_type': food_type,
                            'rating': rating
                            }
                        restaurant_list.append(restaurant)
            except Exception as e:
                raise e
                print('Error, restaurant not found!')
        item_start_number+=1
    return save(restaurant_list)

def save(restaurant_list):
    print("Starting...")
    for restaurant in restaurant_list:
        try:
            Restaurants.objects.create(
                name = restaurant['name'],
                food_type = restaurant['food_type'],
                rating = restaurant['rating']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')


yelp_restaurants()