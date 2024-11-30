from controller.db import conectar_db

def obtener_actividades_activas():
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Selecciona las actividades con is_active en true
            cursor.execute("SELECT nombre FROM activity WHERE is_active = 1")
            resultados = cursor.fetchall()
            
            # Guarda cada actividad en una variable separada
            actividad1 = resultados[0][0] if len(resultados) > 0 else None
            actividad2 = resultados[1][0] if len(resultados) > 1 else None
            actividad3 = resultados[2][0] if len(resultados) > 2 else None
            
            return actividad1, actividad2, actividad3
        
        except Exception as e:
            print(f"Error al obtener actividades activas: {str(e)}")
            return None, None, None
        finally:
            connection.close()
