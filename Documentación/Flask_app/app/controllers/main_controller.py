import mysql.connector

def obtener_ninos():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Ajusta según tu configuración
        database='guarderia_sueno'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM ninos")
    ninos = cursor.fetchall()
    cursor.close()
    connection.close()
    return ninos

def enviar_notificacion(id_nino, mensaje):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Ajusta según tu configuración
        database='guarderia_sueno'
    )
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO notificaciones_sueno (id_nino, fecha, hora_inicio_sueno, hora_fin_sueno, mensaje, tipo_notificacion, estado_notificacion) "
        "VALUES (%s, CURDATE(), NULL, NULL, %s, 'alerta', 'pendiente')",
        (id_nino, mensaje)
    )
    connection.commit()
    cursor.close()
    connection.close()
