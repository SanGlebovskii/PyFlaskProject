"""Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
Модель продукта состоит из id, name, price, amount, comment. На главной странице
отображена краткая информация(id, name, price, amount) по всем продуктам.
При нажатии на продукт происходит перенаправление на детализированную информацию по продукту.
На детализированной странице продукта есть кнопки позволяющие отредактировать и удалить продукт."""
from product_app import app, db
from flask import redirect, render_template, request

from product_app.product import Product


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        product_name = request.form['name']
        product_price = request.form['price']
        product_amount = request.form['amount']
        product = Product(name=product_name, price=product_price, amount=product_amount)
        db.session.add(product)
        db.session.commit()
        return redirect('/')


@app.route('/read', methods=['GET'])
def read_product():
    if request.method == 'GET':
        return Product.query.all()


@app.route('/read/<int:id>', methods=['GET'])
def get_product_by_id():
    if request.method == 'GET':
        return Product.query.get(id)


@app.route('/update', methods=['POST'])
def update_product():
    if request.method == 'POST':
        product_id = request.form['id']
        product_name = request.form['name']
        product_price = request.form['price']
        product_amount = request.form['amount']
        product = Product.query.filter_by(id == product_id).first()
        product.name = product_name
        product.price = product_price
        product.amount = product_amount
        db.session.commit()
        return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_product():
    if request.method == 'POST':
        product_name = request.form['name']
        product_price = request.form['price']
        product_amount = request.form['amount']
        product = Product(name=product_name, price=product_price, amount=product_amount)
        db.session.delete(product)
        db.session.commit()
