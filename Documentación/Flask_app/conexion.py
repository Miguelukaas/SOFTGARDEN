import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Ajusta si es necesario
        database='guarderia_sueno'
    )
    if connection.is_connected():
        print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()
