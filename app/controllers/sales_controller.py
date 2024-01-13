from flask import request , jsonify
from app import db
from sqlalchemy.exc import SQLAlchemyError
from app.models.sales_model import Sale
import logging


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def create_sale():
    try:
        data = request.get_json()

        if "date" not in data or "quantity_in_stock" not in data or "price" not in data:
          return ('missing data fields', 400)
        
        new_sale = Sale(date=data['date'], quantity_in_stock=data['quantity_in_stock'], price=data['price'])
        db.session.add(new_sale)
        db.session.commit()
        return jsonify([new_sale.serialize()])
        

    except SQLAlchemyError as e:
        return handle_error(e,400)
    
def get_sale():
    try:
        sales = Sale.query.all()
        return jsonify ([sale.serialize() for sale in sales])
    
    except SQLAlchemyError as e:
        return (e, 400)
    
def single_sale(id):
    try:
        sales=Sale.query.filter_by(id=id).first()
        return jsonify ([sales.serialize()])
    except SQLAlchemyError as e:
        return (e ,400)
    

def update_sale(id):
    try:
        sales= Sale.query.get(id)
        date= request.json['date']
        quantity_in_stock= request.json['quantity_in_stock']
        price= request.json['price']
        

        sales.date = date
        sales.quantity_in_stock =quantity_in_stock
        sales.price= price

        db.session.commit()
        return jsonify([sales.serialize()])
    except SQLAlchemyError as e:
        return ( e , 400)

    
def delete_sale(id):
    try:
        data = Sale.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return jsonify('deleted successfully', 200)
    
    except SQLAlchemyError as e:
        return ( e , 400)
        