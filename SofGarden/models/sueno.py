from controller.main_controller import conectar_db

def obtener_ninos():
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, nombre FROM ninos")
            ninos = cursor.fetchall()
            cursor.close()
            connection.close()
            return ninos
        except Exception as e:
            print(f"Error al obtener los datos: {str(e)}")
            return None
        finally:
            connection.close()

def enviar_notificacion(id_nino, mensaje):
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO notificaciones_sueno (id_nino, fecha, hora_inicio_sueno, hora_fin_sueno, mensaje, tipo_notificacion, estado_notificacion) "
                "VALUES (%s, CURDATE(), NULL, NULL, %s, 'alerta', 'pendiente')",
                (id_nino, mensaje)
            ) 
        except Exception as e:
            print(f"Error al obtener los datos: {str(e)}")
            return None
        finally:
            connection.close()