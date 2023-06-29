# Define una funcion que alimenta las tablas de la base de datos con los datos de los csv
def fill_tables():
    import psycopg2
    import csv

    # Creamos un bucle para que se intente conectar a la base de datos hasta que lo consiga
    while True: 
        try: 
            connection = psycopg2.connect(host="postgres", dbname="db-ejercicio3", user="postgres", password="postgresadmin")
            mycursor = connection.cursor()
            break
        except(Exception, psycopg2.Error) as error:
                print('Unable to connect', error)


    # Alimentamos las tablas con los datos de los csv
    with open('data/product.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO product (product_id, name) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()

    # Alimentamos las tablas con los datos de los csv
    with open('data/city.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO city (city_id, city_name, country_id) VALUES ('%s', '%s', '%s);" % (row[0], row[1], row[2])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()

    # Alimentamos las tablas con los datos de los csv
    with open('data/store.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO store (store_id, name, city_id) VALUES ('%s', '%s', '%s');" % (row[0], row[1], row[2])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()
    
    # Alimentamos las tablas con los datos de los csv
    with open('data/users.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO users (user_id, name) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()
    
    # Alimentamos las tablas con los datos de los csv
    with open('data/status_name.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO status_name (status_name_id, status_name) VALUES ('%s', '%s');" % (row[0], row[1])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()
    
    # Alimentamos las tablas con los datos de los csv
    with open('data/sale.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO sale (sale_id, amount, date_sale, product_id, user_id, store_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (row[0], row[1], row[2], row[3], row[4], row[5])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()

    # Alimentamos las tablas con los datos de los csv
    with open('data/order_status.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            sql = "INSERT INTO order_status (order_status_id, update_at, sale_id, status_name_id) VALUES ('%s', '%s', '%s', '%s');" % (row[0], row[1], row[2], row[3])
            print(sql)
            try:
                mycursor.execute(sql)
                connection.commit()
            except:
                connection.rollback()

    # Cerramos la conexion SQL
    connection.close() 

# Ejecutamos la funcion
if __name__ == "__main__":
    fill_tables()