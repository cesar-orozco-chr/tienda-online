from flask import Flask, jsonify
from connection.connection import get_sql_alchemy
from model.product import Product
from model.client import Client
from model.purchase import Purchase

app = Flask(__name__)

db = get_sql_alchemy()


@app.route('/product/list', methods=['GET'])
def list_products():
    q = Product.query.filter_by(deleted=False).all()
    '''CREAR JSON PARA EL MODELO PRODUCTO - COMPLEMENTARLO'''
    return jsonify([{'id': p.id, 'sku': p.sku, 'name': p.name} for p in q])


'''INSTANCIAR CREATES RESTANTES CLIENTS Y PURCHASE'''

if __name__ == '__main__':
    app.run(debug=True)
