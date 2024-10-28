from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from controller.activities_controller import ActivitiesController



app = Flask(__name__, template_folder='view')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/microwave_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)




# Instancia del controlador
activities_controller = ActivitiesController()

@app.route('/')
def connect_to_database():
    try:
        # Intenta conectar a la base de datos
        connection = db.engine.connect()
        connection.close()  # Cierra la conexión
        message = "¡Conexión exitosa a la base de datos!"
    except Exception as e:
        message = f"Error al conectar a la base de datos: {str(e)}"

    return render_template('index.html', message=message)

@app.route('/admin')
def admin():
    return render_template('EstadoFisicoAdmin.html')



@app.route('/user')
def user():
    return render_template('EstadoFisico.html')

@socketio.on('select_activity')
def handle_select_activity(data):
    activities_controller.handle_select_activity(data)
    activities_controller.emit_status_update(data)

@socketio.on('send_to_user')
def handle_send_to_user():
    activities_controller.emit_send_to_user()

if __name__ == '__main__':
    socketio.run(app, debug=True)
