from model.activity_model import ActivityModel
from flask_socketio import emit

class ActivitiesController:
    def __init__(self):
        self.activity_model = ActivityModel()

    def handle_select_activity(self, data):
        column = data['column']  # La columna seleccionada
        activity = data['activity']  # La actividad seleccionada
        self.activity_model.update_activity(column, activity)  # Actualizar el estado actual

    def get_current_status(self):
        return self.activity_model.get_current_status()

    def emit_status_update(self, data):
        current_status = self.get_current_status()
        emit('status_updated', {'column': data['column'], 'activity': data['activity']}, broadcast=True)

    def emit_send_to_user(self):
        current_status = self.get_current_status()
        emit('send_to_user', current_status, broadcast=True)
