import requests
import csv
from random import randint
from datetime import datetime, timedelta
from data.fill_tables import fill_tables

# Generamos datos fijos como atributos de clase: product, country, city, store, status_name
class Product:
    def __init__(self, product_id, product_name):
        self.product_id = product_id
        self.product_name = product_name

products = [
    Product(1, 'Product 1'),
    Product(2, 'Product 2'),
    Product(3, 'Product 3'),
    Product(4, 'Product 4')
    ]

# Guardamos los datos de la clase en un csv
csv_file = "data/product.csv"
field_names = ["product_id", "product_name"]
data = [vars(prod) for prod in products] # Convert class instances to dictionaries
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

class Country:
    def __init__(self, country_id, country_name):
        self.country_id = country_id
        self.country_name = country_name

countries = [
    Country(1, 'Spain'),
    Country(2, 'Germany'),
    Country(3, 'UK')
    ]

# Guardamos los datos de la clase en un csv
csv_file = "data/country.csv"
field_names = ["country_id", "country_name"]
data = [vars(country) for country in countries]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)


class City:
    def __init__(self, city_id, city_name, country_id):
        self.city_id = city_id
        self.city_name = city_name
        self.country_id = country_id

cities = [
    City(1, 'Madrid', 1),
    City(2, 'Barcelona', 1),
    City(3, 'Berlin', 2),
    City(4, 'Hamburg', 2),
    City(5, 'London', 3), 
    City(6, 'Liverpool', 3)
    ]

# Guardamos los datos de la clase en un csv
csv_file = "data/city.csv"
field_names = ["city_id", "city_name", "country_id"]
data = [vars(city) for city in cities]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

class Store:
    def __init__(self, store_id, name, city_id):
        self.store_id = store_id
        self.name = name
        self.city_id = city_id

stores = [
    Store(1, 'Store 1', 1),
    Store(2, 'Store 2', 1),
    Store(3, 'Store 3', 2),
    Store(4, 'Store 4', 2),
    Store(5, 'Store 5', 3),
    Store(6, 'Store 6', 3),
    Store(7, 'Store 7', 4),
    Store(8, 'Store 8', 4),
    Store(9, 'Store 9', 5),
    Store(10, 'Store 10', 5),
    Store(11, 'Store 11', 6),
    Store(12, 'Store 12', 6)
    ]

# Guardamos los datos de la clase en un csv
csv_file = "data/store.csv"
field_names = ["store_id", "name", "city_id"]
data = [vars(store) for store in stores]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

class StatusName:
    def __init__(self, status_name_id, status_name):
        self.status_name_id = status_name_id
        self.status_name = status_name

status_names = [
    StatusName(1, 'Pending Payment'),
    StatusName(2, 'Shipped'),
    StatusName(3, 'Delivered')
    ]

# Guardamos los datos de la clase en un csv
csv_file = "data/status_name.csv"
field_names = ["status_name_id", "status_name"]
data = [vars(status_name) for status_name in status_names]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)


# Generamos n clientes con la API randomuser.me
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

n = 20
users = []
for i in range(n):
        URL = "https://randomuser.me/api/"
        #connectamos a la API un par de veces para evitar errores (freezing problem)
        try:
            respuesta = requests.get(URL,timeout=3)
        except requests.exceptions.Timeout as err:
            print(err)
        if respuesta.status_code >= 200 and respuesta.status_code < 300:
            data = respuesta.json()
            users.append(User(id(i), data["results"][0]["name"]["first"]))

# Guardamos los datos de la clase en un csv
csv_file = "data/users.csv"
field_names = ["user_id", "name"]
data = [vars(user) for user in users]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

# Generamos m datos aleatorios como atributos de clase: sale
class Sale:
    def __init__(self, sale_id, amount, date_sale, product_id, user_id, store_id):
        self.sale_id = sale_id
        self.amount = amount
        self.date_sale = date_sale
        self.product_id = product_id
        self.user_id = user_id
        self.store_id = store_id

m = 100
sales = []

for i in range(m):
    sale_id = i
    amount = randint(1, 100)
    date_sale = datetime.now() - timedelta(days=randint(1, 100))
    product_id = randint(1, len(products))
    user_id = randint(1, len(name))
    store_id = randint(1, len(stores))
    sales.append(Sale(sale_id, amount, date_sale, product_id, user_id, store_id))

# Guardamos los datos de la clase en un csv
csv_file = "data/sale.csv"
field_names = ["sale_id", "amount", "date_sale", "product_id", "user_id", "store_id"]
data = [vars(sale) for sale in sales]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

# Generamos datos aleatorios como atributos de clase: status_order
class OrderStatus:
    def __init__(self, order_status_id, update_at, sale_id, status_name_id):
        self.order_status_id = order_status_id
        self.update_at = update_at
        self.sale_id = sale_id
        self.status_name_id = status_name_id

order_status = []
for i in range(m):
    order_status_id = i
    sale_id = i
    update_at = datetime.now() - timedelta(days=randint(1, 100))
    status_name_id = randint(1, len(status_names))
    order_status.append(OrderStatus(order_status_id, update_at, sale_id, status_name_id))

# Guardamos los datos de la clase en un csv
csv_file = "data/order_status.csv"
field_names = ["order_status_id", "update_at", "sale_id", "status_name_id"]
data = [vars(order_status) for order_status in order_status]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
    
# Llamamos a la función que alimenta las tablas con los datos de los csv
fill_tables()