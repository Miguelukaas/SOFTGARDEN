# run.py

from flask import Flask, Blueprint
from app.views.health_view import health_bp

app = Flask(__name__)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(debug=True)

