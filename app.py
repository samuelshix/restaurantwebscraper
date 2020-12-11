import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
    conn.close()
    return render_template('index.html', restaurants=restaurants)

@app.route('/about.html')
def about():
    return render_template('about.html')