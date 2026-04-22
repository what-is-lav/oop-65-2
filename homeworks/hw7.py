import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
''')
connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        'INSERT INTO products (name, price, quantity) VALUES (?,?,?)',
        (name, price, quantity)
    )
    connect.commit()
    print(f'Товар "{name}" добавлен!')

create_product("Банан", 30, 100)
create_product("Яблоко", 28, 100)
create_product("Груша", 24, 100)

def read_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    print("\nВсе товары:")
    for product in products:
        print(product)
    print()
read_products()

def update_product(id, new_price):
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (new_price, id)
    )
    connect.commit()
    print(f"Цена товара с id={id} обновлена!")
update_product(2, 35)
read_products()

def delete_product(id):
    cursor.execute(
        'DELETE FROM products WHERE id = ?',
        (id,)
    )
    connect.commit()
    print(f'Товар с id={id} удален!')

delete_product(1)
read_products()
connect.close()