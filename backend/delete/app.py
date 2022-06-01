#backend.delete
from flask import  request
from connection import db, create_app
from model.product import Product
from model.client import Client
from model.purchase import Purchase

app = create_app()


@app.route('/product/delete/<int:id>', methods=['POST'])
def delete_product(id):
    if request.method == 'POST':
        p = Product.query.get(id)
        if p is not None and p.state != "inactivo":
            p.state = "inactivo"
            db.session.add(p)
            db.session.commit()
            return "Producto Borrado!", 200
        else:
            return "Producto No Encontrado/Ya Eliminado", 402


if __name__ == '__main__':
    app.run(debug=True, port='8081')
