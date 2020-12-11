DROP TABLE IF EXISTS restaurants;

CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    food_type TEXT NOT NULL,
    rating FLOAT NOT NULL,
    address TEXT NOT NULL
)