from controller.db_alimentacion import conectar_db  # Importamos la función de conexión a la base de datos

def cambiar_activo(menu_id):
    try:
        # Establecemos la conexión a la base de datos
        connection = conectar_db()
        cursor = connection.cursor()

        # Creamos la consulta SQL para actualizar el valor de 'ACTIVO' a TRUE
        sql = "UPDATE menus SET ACTIVO = TRUE WHERE ID = %s"
        
        # Ejecutamos la consulta con el ID del menú
        cursor.execute(sql, (menu_id,))

        # Confirmamos los cambios
        connection.commit()

        # Cerramos la conexión
        cursor.close()
        connection.close()

        # Retornamos un mensaje de éxito
        return f"El menú con ID {menu_id} ha sido activado exitosamente.", 200

    except Exception as e:
        # Si ocurre un error, mostramos un mensaje
        return f"Ocurrió un error al activar el menú con ID {menu_id}. Error: {str(e)}", 500
