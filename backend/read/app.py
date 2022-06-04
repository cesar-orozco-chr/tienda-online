from flask import jsonify, render_template, url_for
from connection import create_app
from model.product import Product
from model.client import Client
from model.purchase import Purchase

app = create_app('templates')


@app.route('/product/list', methods=['GET'])
def list_products():
    q = Product.query.all()
    # return jsonify([{'id': p.id, 'sku': p.sku, 'name': p.name} for p in q])
    l = [{'id': p.id, 'sku': p.sku, 'name': p.name} for p in q]
    # l = [i for i in range(5)]
    return render_template('product.html', products=l)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
