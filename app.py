from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configura a URI do banco de dados para SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# Cria a instância da extensão SQLAlchemy e a associa à aplicação Flask
db = SQLAlchemy(app)

## Modelo
# Produto

# Definindo um modelo de exemplo
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'


@app.route('/api/products/add', methods=["POST", "GET"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get('description', ''))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully!'}), 200
    return jsonify({'message': 'Invalid product data'}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    #Recuperar o produto da base de dados
    #Verificar se o produto existe
    #Se existir, apagar da base de dados
    #Caso não exista, retornar erro 404 (not found)
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully!'}), 200
    return jsonify({'message': 'Product not found!'}), 404


# Definir uma rota raiz (página inicial)
@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
