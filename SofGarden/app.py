from flask import Flask, render_template, request, redirect, url_for
from models.actualizar_activity import actualizar_estado_actividad  
from models.obtener_activity import obtener_actividades_activas
from models.cambiar_activo import cambiar_activo
from models.obtener_menu import obtener_menu_activo
from models.carnet_model import obtener_datos
from models.sueno import obtener_ninos, enviar_notificacion


app = Flask(__name__, template_folder='view')
#MICROSERVICIO ESTADO FISICO -------------------------------------------------------------------------------------------
@app.route('/admin')
def admin_page():
    return render_template('EstadoFisicoAdmin.html')

@app.route('/actualizar_actividad', methods=['POST'])
def actualizar_actividad():
    # Obtén el id de la actividad del cuerpo de la solicitud
    activity_id = request.form.get('activity_id')
    
    if activity_id:
        # Llama a la función para actualizar el estado de la actividad
        actualizar_estado_actividad(activity_id)
        return "Actividad actualizada correctamente", 200
    else:
        return "ID de actividad no proporcionado", 400

@app.route('/estadofisico')
def estado_fisico_usuario():
    actividad1, actividad2, actividad3 = obtener_actividades_activas()
    return render_template('EstadoFisico.html', actividad1=actividad1, actividad2=actividad2, actividad3=actividad3)

#MICROSERVICIO DE ALIMENTACION-------------------------------------------------------------------------------------------

@app.route('/alimentacion')
def home():
    return render_template('alimentacion.html')  # Renderiza la plantilla "alimentacion.html"

@app.route('/cambiar_activo', methods=['POST'])
def cambiar_activo_route():
    menu_id = request.form.get('menu_id')  # Obtenemos el ID del menú desde el frontend

    # Llamamos a la función cambiar_activo de model/cambiar_activo.py
    mensaje, codigo = cambiar_activo(menu_id)

    return mensaje, codigo  # Retornamos el mensaje y el código de estado

@app.route('/menu_usuario')
def menu_usuario():
    menu_id = obtener_menu_activo()

    if menu_id:
        # Si hay un menú activo, seleccionamos la imagen correspondiente
        menu_imagen = f"menu{menu_id}.jpg"
    else:
        # Si no hay menú activo, mostramos una imagen predeterminada o un mensaje
        menu_imagen = "default.jpg"
    
    # Renderizamos el template con la imagen
    return render_template('usuario_alimentacion.html', menu_imagen=menu_imagen)


#MICROSERVICIO SALUD Y BIENESTAR----------------------------------------------------------------------------------------

@app.route('/carnetUsuario')
def carnet_bebe():
    # Obtener los datos de la base de datos
    datos = obtener_datos()
    if datos is not None:
        return render_template("carnetUsuario.html", datos=datos)
    else:
        return "Error al obtener los datos."

#MICROSERVICIO SUEÑO---------------------------------------------------------
@app.route('/sueno', methods=['GET'])
def index():
    # Obtener la lista de niños desde la base de datos
    ninos = obtener_ninos()
    return render_template('index.html', ninos=ninos)

@app.route('/enviar', methods=['POST'])
def enviar():
    # Obtener datos del formulario
    id_nino = request.form['id_nino']
    mensaje = request.form['mensaje']

    # Enviar notificación
    enviar_notificacion(id_nino, mensaje)

    # Redirigir al index después de enviar
    return redirect(url_for('index'))

@app.route('/indice')
def indice():
    return render_template('indiceNuevo.html')


@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/login')
def login():
    return redirect("http://localhost:/SoftGarden/login.html")

if __name__ == "__main__":
    app.run(debug=True)


