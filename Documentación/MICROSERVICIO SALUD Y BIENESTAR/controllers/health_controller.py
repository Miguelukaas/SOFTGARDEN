# /app/controllers/health_controller.py

from flask import request, jsonify
from app.models.health_model import get_all_records, get_record_by_baby_id, add_health_record, update_health_record

def get_health_records():
    records = get_all_records()
    return jsonify({'health_records': records})

def get_health_record(baby_id):
    record = get_record_by_baby_id(baby_id)
    if not record:
        return jsonify({'message': 'Registro de salud no encontrado'}), 404
    return jsonify({'health_record': record})

def create_health_record():
    data = request.json
    new_record = add_health_record(
        baby_id=data.get('baby_id'),
        vaccines=data.get('vaccines', []),
        illnesses=data.get('illnesses', []),
        medication=data.get('medication', []),
        observations=data.get('observations', '')
    )
    return jsonify({'health_record': new_record}), 201

def edit_health_record(baby_id):
    data = request.json
    record = update_health_record(
        baby_id,
        vaccines=data.get('vaccines'),
        illnesses=data.get('illnesses'),
        medication=data.get('medication'),
        observations=data.get('observations')
    )
    if not record:
        return jsonify({'message': 'Registro de salud no encontrado'}), 404
    return jsonify({'health_record': record})

# /app/controllers/health_controller.py
from flask import request, jsonify, render_template
from app.models.health_model import get_all_records, get_record_by_baby_id, add_health_record, update_health_record

def get_health_records():
    records = get_all_records()
    return render_template('health_records.html', health_records=records)
