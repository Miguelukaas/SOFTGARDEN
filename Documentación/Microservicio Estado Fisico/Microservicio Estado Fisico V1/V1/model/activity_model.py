class ActivityModel:
    def __init__(self):
        self.current_status = {
            "activities": ["", "", ""],  # Para 3 columnas
        }

    def update_activity(self, column, activity):
        self.current_status['activities'][column] = activity

    def get_current_status(self):
        return self.current_status
