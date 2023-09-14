from flask import Flask,render_template, request, url_for, redirect

index = Flask(__name__)

@index.route("/")
def hello_world():#defino una funcion
    lista=['e1','e2','e3']
    data={
        'titulo': 'Proyecto Flask',
        'bienvenida': 'saludos!',
        'lista': lista,
        'largo_lista': len(lista)
    }
    return render_template('index.html',data=data) #retorno un contenido
@index.route('/contacto/<nombre>/<int:edad>')

def contacto(nombre,edad):
    data={
        'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html',data=data)
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'ok'

def pagina_no_encontrada(error):
    #return render_template('404.html'),404
    return redirect(url_for('index'))

if __name__=="__main__":
    index.add_url_rule('/query_string', view_func=query_string)
    index.register_error_handler(404,pagina_no_encontrada)
    index.run(debug=True)