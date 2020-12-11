import json

article_list = ['a','b','c']
def save(article_list):
    with open('restaurants.txt', 'w') as outfile:
        json.dump(article_list, outfile)
save(article_list)