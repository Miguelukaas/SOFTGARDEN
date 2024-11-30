from controller.dbSoftGarden import conectar_db

def save_user(nombre, correo, contrasena):
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO usuario(nombre, correo, contrasena, id_cargo) VALUES(%s, %s, %s, %s)"
            cursor.execute(query, (nombre, correo, contrasena, '3'))
            connection.commit()
            cursor.close()
            connection.close()
            return True  # Indicando que la operación fue exitosa
        except Exception as e:
            print(f"Error al guardar el usuario: {str(e)}")
            return False  # Indicando que la operación falló
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    return False  # Indicando que la conexión a la base de datos falló
