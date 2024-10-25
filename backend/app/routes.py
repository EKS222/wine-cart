from flask import jsonify, request, Blueprint
from .models import db, User, Wine, Cart
from flask_bcrypt import Bcrypt
from flask import current_app as app
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging

routes = Blueprint('routes', __name__)
bcrypt = Bcrypt()

logging.basicConfig(level=logging.DEBUG)

@routes.route('/')
def home():
    return jsonify({"message": "wine-app-api"})


# -------------------------
# User CRUD Operations
# -------------------------

# Get all users
@routes.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.all()
    serialized_users = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phonenumber': user.phonenumber,
            'created_at': user.created_at
        }
        for user in users
    ]
    return jsonify({'users': serialized_users}), 200


# Create a new user
@routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()

    # Validate required fields
    if not all(key in user_data for key in ('username', 'email', 'password')):
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if user exists
    if User.query.filter_by(email=user_data['email']).first():
        return jsonify({'message': 'User with this email already exists'}), 400

    hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
    new_user = User(
        username=user_data['username'],
        email=user_data['email'],
        password=hashed_password,
        phonenumber=user_data.get('phonenumber')
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201


# Update user
@routes.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user_data = request.get_json()
    user = User.query.get(user_id)

    if user:
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        if 'password' in user_data:
            user.password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        user.phonenumber = user_data.get('phonenumber', user.phonenumber)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


# Delete user
@routes.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


# -------------------------
# Wine CRUD Operations
# -------------------------

# Get all wines
@routes.route('/wines', methods=['GET'])
def get_all_wines():
    wines = Wine.query.all()
    serialized_wines = [
        {
            'id': wine.id,
            'name': wine.name,
            'description': wine.description,
            'price': wine.price,
            'created_at': wine.created_at
        }
        for wine in wines
    ]
    return jsonify({'wines': serialized_wines}), 200


# Create a new wine
@routes.route('/wines', methods=['POST'])
@jwt_required()
def create_wine():
    wine_data = request.get_json()
    new_wine = Wine(
        name=wine_data['name'],
        description=wine_data.get('description'),
        price=wine_data['price']
    )
    db.session.add(new_wine)
    db.session.commit()
    return jsonify({'message': 'Wine created successfully', 'wine_id': new_wine.id}), 201


# Update wine
@routes.route('/wines/<int:wine_id>', methods=['PUT'])
@jwt_required()
def update_wine(wine_id):
    wine_data = request.get_json()
    wine = Wine.query.get(wine_id)

    if wine:
        wine.name = wine_data.get('name', wine.name)
        wine.description = wine_data.get('description', wine.description)
        wine.price = wine_data.get('price', wine.price)
        db.session.commit()
        return jsonify({'message': 'Wine updated successfully'}), 200
    return jsonify({'message': 'Wine not found'}), 404


# Delete wine
@routes.route('/wines/<int:wine_id>', methods=['DELETE'])
@jwt_required()
def delete_wine(wine_id):
    wine = Wine.query.get(wine_id)
    if wine:
        db.session.delete(wine)
        db.session.commit()
        return jsonify({'message': 'Wine deleted successfully'}), 200
    return jsonify({'message': 'Wine not found'}), 404


# -------------------------
# Cart CRUD Operations
# -------------------------

# Get all items in the user's cart
@routes.route('/cart', methods=['GET'])
@jwt_required()
def get_cart_items():
    user_id = get_jwt_identity()
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    serialized_cart = [
        {
            'id': item.id,
            'wine_id': item.wine_id,
            'quantity': item.quantity
        }
        for item in cart_items
    ]
    return jsonify({'cart': serialized_cart}), 200


# Add a wine to the cart
@routes.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    cart_data = request.get_json()
    wine_id = cart_data['wine_id']
    quantity = cart_data.get('quantity', 1)

    # Check if item is already in cart
    cart_item = Cart.query.filter_by(user_id=user_id, wine_id=wine_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=user_id, wine_id=wine_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({'message': 'Wine added to cart'}), 201


# Update cart item quantity
@routes.route('/cart/<int:cart_item_id>', methods=['PUT'])
@jwt_required()
def update_cart_item(cart_item_id):
    cart_data = request.get_json()
    cart_item = Cart.query.get(cart_item_id)

    if cart_item and cart_item.user_id == get_jwt_identity():
        cart_item.quantity = cart_data.get('quantity', cart_item.quantity)
        db.session.commit()
        return jsonify({'message': 'Cart item updated successfully'}), 200
    return jsonify({'message': 'Cart item not found or unauthorized'}), 404


# Delete item from cart
@routes.route('/cart/<int:cart_item_id>', methods=['DELETE'])
@jwt_required()
def delete_cart_item(cart_item_id):
    cart_item = Cart.query.get(cart_item_id)
    if cart_item and cart_item.user_id == get_jwt_identity():
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Cart item deleted successfully'}), 200
    return jsonify({'message': 'Cart item not found or unauthorized'}), 404
