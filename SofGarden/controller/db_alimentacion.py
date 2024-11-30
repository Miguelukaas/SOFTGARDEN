import mysql.connector


def conectar_db():
    """Función para establecer la conexión a la base de datos MySQL"""
    try:
        # Configura los parámetros de conexión (ajústalos según tu base de datos)
        connection = mysql.connector.connect(
            host='localhost',        # Dirección del servidor MySQL (puede ser una IP o localhost)
            user='root',             # Tu usuario de MySQL
            password='',# Tu contraseña de MySQL
            database='alimentacion_db'  # El nombre de tu base de datos
        )
        return connection 
    except mysql.connector.Error as e: 
        print(f"Error al conectar la base de datos: {str(e)}")
        return None 
    
        
        
