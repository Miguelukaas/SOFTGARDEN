from controller.db_alimentacion import conectar_db

def obtener_menu_activo():
    """Función para obtener el menú activo de la base de datos."""
    try:
        # Establecemos la conexión a la base de datos
        connection = conectar_db()
        cursor = connection.cursor()

        # Consultamos los menús activos
        sql = "SELECT ID FROM menus WHERE ACTIVO = TRUE"
        cursor.execute(sql)

        # Obtenemos los resultados
        resultado = cursor.fetchone()

        # Cerramos la conexión
        cursor.close()
        connection.close()

        if resultado:
            menu_id = resultado[0]
            # Retornamos el ID del menú activo
            return menu_id
        else:
            # Si no hay ningún menú activo, retornamos None
            return None
    except Exception as e:
        print(f"Error al obtener el menú activo: {str(e)}")
        return None
