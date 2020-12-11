import sqlite3
from index import yelp_restaurants

restaurant_list = yelp_restaurants()

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for i in range(len(restaurant_list)):
    cur.execute("INSERT INTO restaurants (name, food_type, rating, address) VALUES (?, ?, ?, ?)",
                (restaurant_list[i]['name'], restaurant_list[i]['food_type'],float(restaurant_list[i]['rating'][:3]),restaurant_list[i]['address']))
connection.commit()
connection.close()