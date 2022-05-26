from flask import Flask, request
from connection.connection import get_sql_alchemy
from model.product import Product
from model.client import Client
from model.purchase import Purchase

app = Flask(__name__)

db = get_sql_alchemy()


@app.route('/product/delete/<int:id>', methods=['POST'])
def delete_product(id):
    if request.method == 'POST':
        p = Product.query.get(id)
        if p is not None:
            p.deleted = 1
            db.session.add(p)
            db.session.commit()
            return "Product Deleted!", 200
        else:
            return "Product Not Found", 402


'''INSTANCIAR CREATES RESTANTES CLIENTS Y PURCHASE'''

if __name__ == '__main__':
    app.run(debug=True)
