from flask import Blueprint
from app.controllers.user_controller import create_user, get_users
from app.controllers.car_controller import create_car, get_cars, get_car, update_car, delete_car
from app.controllers.sales_controller import create_sale,get_sale, delete_sale, single_sale, update_sale
bp = Blueprint('bp', __name__)

@bp.route('/users', methods=['POST'])
def add_user():
    return create_user()

@bp.route('/users', methods=['GET'])
def list_users():
    return get_users()

@bp.route('/cars', methods=['POST'])
def add_car():
    return create_car()

@bp.route('/cars', methods=['GET'])
def list_cars():
    return get_cars()

@bp.route('/cars/<int:car_id>')
def list_car(car_id):
    return (get_car(car_id))

@bp.route('/cars/<int:car_id>', methods=['PUT'])
def updated_car(car_id):
    return (update_car(car_id))

@bp.route('/cars/<int:id>', methods=['DELETE'])
def deleted_car(id):
    return (delete_car(id))

@bp.route('/sale', methods= ['POST'])
def created_sale():
    return (create_sale())

@bp.route('/sale')
def list_sale():
    return (get_sale())

@bp.route('/sale/<int:id>')
def get_single_sale(id):
    return (single_sale(id))

@bp.route('/sale/<int:id>', methods=['PUT'])
def updated_sale(id):
    return (update_sale(id))


@bp.route ('/sale/<int:id>', methods=['DELETE'])
def deleted_sale(id):
    return (delete_sale(id))