from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def index():

    return render_template('home.html')

@app.route("/contatos")

def contatos():

    return render_template('contatos.html')

@app.route('/formulario')
def formulario():
    return render_template('formularios.html')