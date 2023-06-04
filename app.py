from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

import sqlite3

app = Flask(__name__)
db_path = 'inventory.db'


def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       stock INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products



def add_product(name, stock):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, stock) VALUES (?, ?)", (name, stock))
    conn.commit()
    conn.close()

def update_product_stock(name, stock):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = ? WHERE name = ?", (stock, name))
    conn.commit()
    conn.close()

def remove_product(name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE name = ?", (name,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    products = get_all_products()
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product_route():
    name = request.form['name']
    stock = int(request.form['stock'])
    add_product(name, stock)
    return redirect('/')



@app.route('/update_stock', methods=['POST'])
def update_stock_route():
    name = request.form['name']
    stock = int(request.form['stock'])
    update_product_stock(name, stock)
    return redirect('/')

@app.route('/remove_product', methods=['POST'])
def remove_product_route():
    name = request.form['name']
    remove_product(name)
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
