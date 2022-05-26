from flask import Flask, request
from connection.connection import get_sql_alchemy
from model.product import Product
from model.client import Client
from model.purchase import Purchase
import json

app = Flask(__name__)

db = get_sql_alchemy()


@app.route('/product/edit/<int:id>', methods=['POST'])
def edit_product(id):
    if request.method == 'POST':
        p = Product.query.get(id)
        d = json.loads(request.data)

        if p is not None:
            '''SETEAR NUEVOS VALORES DEL PRODUCTO'''
            '''
            p.sku = d['sku']
            p.name = d['name']
            '''
            db.session.add(p)
            db.session.commit()

            return "Product Updated", 200
        else:

            return "Product Not Found", 402


'''INSTANCIAR CREATES RESTANTES CLIENTS Y PURCHASE'''

if __name__ == '__main__':
    app.run(debug=True)
