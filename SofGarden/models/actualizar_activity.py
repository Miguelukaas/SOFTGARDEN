from controller.db import conectar_db 

def actualizar_estado_actividad(activity_id):
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Desactivar todas las actividades de la misma categoría
            cursor.execute("UPDATE activity SET is_active = 0 WHERE categoria_id = (SELECT categoria_id FROM activity WHERE id = %s)", (activity_id,))
            # Activar la nueva actividad
            cursor.execute("UPDATE activity SET is_active = 1 WHERE id = %s", (activity_id,))
            connection.commit()  # Confirma los cambios
            print("Actividad actualizada correctamente.")
        except Exception as e:
            print(f"Error al actualizar la actividad: {str(e)}")
            connection.rollback()  # Deshacer cambios en caso de error
        finally:
            connection.close()  # Cierra la conexión

