# /app/views/health_view.py

from flask import Blueprint
from app.controllers.health_controller import get_health_records, get_health_record, create_health_record, edit_health_record

health_bp = Blueprint('health_bp', __name__)

health_bp.route('/health_records', methods=['GET'])(get_health_records)
health_bp.route('/health_records/<int:baby_id>', methods=['GET'])(get_health_record)
health_bp.route('/health_records', methods=['POST'])(create_health_record)
health_bp.route('/health_records/<int:baby_id>', methods=['PUT'])(edit_health_record)

# /app/views/health_view.py
from flask import Blueprint
from app.controllers.health_controller import get_health_records, get_health_record, create_health_record, edit_health_record

health_bp = Blueprint('health_bp', __name__)

health_bp.route('/health_records', methods=['GET'])(get_health_records)
health_bp.route('/health_records/<int:baby_id>', methods=['GET'])(get_health_record)
health_bp.route('/health_records', methods=['POST'])(create_health_record)
health_bp.route('/health_records/<int:baby_id>', methods=['PUT'])(edit_health_record)
