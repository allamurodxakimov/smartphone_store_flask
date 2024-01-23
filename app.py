from flask import Flask, request, jsonify
from db import SmartphoneDB


app = Flask(__name__)
db = SmartphoneDB('db.json')


## view all smartphone
@app.route('/')
def Home():
    return "Hello students, I have phone"

@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    """Returns all smartphones in the database"""
    return db.all_smartphone()


# view all brands
@app.route('/smartphones/brands', methods=['GET'])
def get_all_brands():
    """Returns all brands in the database"""
    return db.brands()


# view all smartphones by brand
@app.route('/smartphones/<brand>', methods=['GET'])
def get_smartphone_by_brand(brand):
    """Returns all products by brand"""
    return db.get_smartphone_by_brand(brand)


# view smartphone by name
@app.route('/smartphones/name/<name>', methods=['GET'])
def get_smartphone_by_name(name):
    """Returns a product by name"""
    return db.get_smartphone_by_name(name)


# view smartphone by price
@app.route('/smartphones/price/<price>', methods=['GET'])
def get_smartphone_by_price(price):
    """Returns a product by price"""
    return db.get_smartphone_by_price(price)

# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    if request.method=="POST":
        smartpone = request.get_json()
    brand = "Apple"
    return db.add_smartphone(brand=brand, smartphone=smartpone)


# view delete smartphone
@app.route('/smartphone/delete/<brand>/<int:doc_id>', methods=['DELETE'])
def delete_smartphone(brand, doc_id):
    """Deletes a product from the database"""
    return db.delete_smartphone(brand=brand, doc_id=doc_id)


if __name__ == '__main__':
    app.run(debug=True)