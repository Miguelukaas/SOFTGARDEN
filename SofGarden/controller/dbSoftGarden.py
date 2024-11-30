import mysql.connector

def conectar_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Asegúrate de poner tu contraseña aquí si tienes
            database='registro_guarderia'
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        return None