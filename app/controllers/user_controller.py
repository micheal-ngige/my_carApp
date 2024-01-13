from flask import request, jsonify
from app import db
from app.models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def create_user():
    try:
        data = request.get_json()

        if 'username' not in data or 'email' not in data or 'usertype' not in data:
            return handle_error('Missing data fields (username, email, usertype required)', 400)
        
        new_user = User(username=data['username'], email=data['email'], usertype=data['usertype'])
        db.session.add(new_user)
        db.session.commit()
        logging.info(jsonify(new_user.serialize()))
        return jsonify(new_user.serialize()), 201
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_users():
    try:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    
    except SQLAlchemyError as e:
        return handle_error(e, 500)

def get_user(user_id):
    return

def update_user(user_id):
    return

def delete_user(user_id):
    return
