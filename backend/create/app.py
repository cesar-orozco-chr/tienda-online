#backend.create
from flask import request
from connection import db, create_app
from model.product import Product

import json

app = create_app()


@app.route('/product/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        r = json.loads(request.data)
        product = Product(
            r["productid"],
            r["name"],
            r["price"]
        )
        db.session.add(product)
        db.session.commit()

        return "Producto Agregado", 200


if __name__ == '__main__':
    app.run(debug=True, port='8080')
