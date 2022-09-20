from flask import *
app = Flask(__name__)

@app.route('/')
def home():
   template_data = {
      'titulo' : 'Esto es Python en Ada',
   }
   html = """
   <h1>esta es mi primera web</h1>
   <h2>la hicimos con el capo de jere</h2>
    """
   return html
   return render_template('home.html', **template_data)
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)

