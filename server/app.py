from flask import *
import datetime

app = Flask(__name__)
# welcome

# route => url/method

# match
"""
@app.route('/')
def home():
    context = {
        'titulo': 'Flask Server',
        'clase': '17',
        'hora': '19:55'
    }
    return render_template('home.html', **context)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/sing-up')
def sign_up():
    nombre = param[0]
    base_datos.create(user)
    return 'usuario creado'
    pass
"""

@app.route('/')
def inicio():
    #return 'Página principal'   
    return render_template('home.html')

@app.route('/articulos/')
def articulos():
    return 'Lista de artículos' 

@app.route("/articulos/<int:id>")
def mostrar_ariculo(id):
    return 'Vamos a mostrar el artículo con id:{}'.format(id)

@app.route('/acercade')
def acercade():
    return 'Página acerca de...'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)