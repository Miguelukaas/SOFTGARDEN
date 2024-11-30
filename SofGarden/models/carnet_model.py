from controller.db_saludybienestar import conectar_db

def obtener_datos():
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Selecciona todos los registros de la tabla carnet_salud_bebe
            cursor.execute("SELECT ID_Bebe, Nombre, Fecha_Nacimiento, Peso, Altura, Medicamento, Observaciones FROM carnet_salud_bebe")
            resultados = cursor.fetchall()
            print(resultados)  # Verifica los datos obtenidos

            return resultados
        
        except Exception as e:
            print(f"Error al obtener los datos: {str(e)}")
            return None
        finally:
            connection.close()


