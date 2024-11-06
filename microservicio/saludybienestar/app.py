from flask import Flask, render_template
from model.carnet_model import obtener_datos

app = Flask(__name__, template_folder="view")

@app.route('/')
def carnet_bebe():

    return render_template("carnetUsuario.html")

if __name__ == "__main__":
    app.run(debug=True)
