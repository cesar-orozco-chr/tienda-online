from flask import request
from connection import db, create_app
from model.product import Product
from model.client import Client
from model.purchase import Purchase

import json

app = create_app()


@app.route('/product/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        r = json.loads(request.data)
        product = Product(
            '''INSTANCIAR OBJETO PRODUCTO'''
        )
        db.session.add(product)
        db.session.commit()

        return "New Product Added", 200


'''INSTANCIAR CREATES RESTANTES CLIENTS Y PURCHASE'''

if __name__ == '__main__':
    app.run(debug=True)
