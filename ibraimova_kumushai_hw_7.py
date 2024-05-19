import sqlite3


conn = sqlite3.connect('hw.db')
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_title TEXT NOT NULL,
                price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
                quantity INTEGER DEFAULT 0 NOT NULL
            )''')


def add_products():
    products = [
        ("Жидкое мыло с запахом ванили", 50.99, 10),
        ("Мыло детское", 35.50, 20),
        ("Шампунь для волос", 120.75, 15),
        ("Зубная паста", 80.25, 25),
        ("Спрей для тела", 150.00, 8),
        ("Крем для рук", 70.20, 30),
        ("Масло для волос", 200.50, 12),
        ("Дезодорант", 90.99, 18),
        ("Гель для душа", 60.30, 22),
        ("Кондиционер для волос", 180.25, 14),
        ("Туалетная бумага", 40.50, 40),
        ("Крем для лица", 100.00, 20),
        ("Губная помада", 75.75, 16),
        ("Пена для бритья", 85.20, 25),
        ("Очищающий гель", 55.99, 30)
    ]
    cur.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()

def change_quantity(product_id, new_quantity):
    cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()

def change_price(product_id, new_price):
    cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()

def print_all_products():
    cur.execute("SELECT * FROM products")
    all_products = cur.fetchall()
    for product in all_products:
        print(product)

def print_products_below_limit():
    cur.execute("SELECT * FROM products WHERE price < 100 AND quantity > 5")
    products_below_limit = cur.fetchall()
    for product in products_below_limit:
        print(product)


def search_products_by_title(title):
    cur.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + title + '%',))
    search_result = cur.fetchall()
    for product in search_result:
        print(product)


add_products()

print("\nДобавленные товары:")
print_all_products()

change_quantity(1, 5)
print("\nИзмененное количество товара с id=1:")
print_all_products()

change_price(2, 40.00)
print("\nИзмененная цена товара с id=2:")
print_all_products()

delete_product(3)
print("\nУдален товар с id=3:")
print_all_products()

print("\nТовары дешевле лимита и с количеством больше лимита остатка на складе:")
print_products_below_limit()

print("\nПоиск товаров по названию 'мыло':")
search_products_by_title("мыло")

conn.close()
