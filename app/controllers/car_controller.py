from flask import request, jsonify
from app import db
from app.models.car_model import Car
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def create_car():
    try:
        data = request.get_json()

        if 'make' not in data or 'model' not in data or 'year' not in data or 'user_id' not in data:
            return handle_error('Missing data fields', 400)
        
        new_car = Car(make=data['make'], model=data['model'], year=data['year'], user_id=data['user_id'])
        db.session.add(new_car)
        db.session.commit()
        logging.info(jsonify(new_car.serialize()))
        return jsonify(new_car.serialize()), 201
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_cars():
    try:
        cars = Car.query.all()
        return jsonify([car.serialize() for car in cars]), 200
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_car(car_id):
    try:
        car = Car.query.filter_by(id=car_id).first()
        return jsonify([car.serialize()]), 200   
           
    except SQLAlchemyError as e:
        return handle_error(e, 500)  
    
def update_car(id):
    try:
        car = Car.query.get(id)
        make = request.json['make']
        model = request.json['model']
        year = request.json['year']
        user_id = request.json['user_id']

        car.make= make
        car.model= model
        car.year = year
        car.user_id = user_id
    
        db.session.commit()
        return jsonify([car.serialize()]), 201    

    except SQLAlchemyError as e:
        return handle_error(e, 500)  
    
def delete_car(car_id):
    try:
        car = Car.query.get(car_id)

        if not car:
            return jsonify({'error': 'Car not found'}), 404

        db.session.delete(car)
        db.session.commit()

        return jsonify({'message': 'Car deleted successfully'}), 200

    except SQLAlchemyError as e:
        return handle_error(e, 500)

      

        
    
           

   
    


   
    


    

