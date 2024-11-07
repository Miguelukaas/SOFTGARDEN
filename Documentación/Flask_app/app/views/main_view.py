from flask import Blueprint, render_template, request, redirect, url_for
from ..controllers.main_controller import obtener_ninos, enviar_notificacion

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    ninos = obtener_ninos()
    return render_template('index.html', ninos=ninos)

@main_bp.route('/enviar', methods=['POST'])
def enviar():
    id_nino = request.form['id_nino']
    mensaje = request.form['mensaje']
    enviar_notificacion(id_nino, mensaje)
    return redirect(url_for('main.index'))
