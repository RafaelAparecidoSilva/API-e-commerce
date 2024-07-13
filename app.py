from flask import Flask

# Instanciação do aplicativo do flask
app = Flask(__name__)


# Definir uma rota raiz (página inicial)
@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)