from flask import jsonify, request, Blueprint
from .models import db, User,WineTypes, Regions, Varietals, Wines
from . import db
from flask_bcrypt import Bcrypt
from flask import current_app as app
import logging

routes = Blueprint('routes', __name__)
bcrypt = Bcrypt()


logging.basicConfig(level=logging.DEBUG)


@routes.route('/')
def home():
    data = {"message": "wine-app-api"}
    return jsonify(data)
# Route to get all users
## Get Method 
@routes.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    serialized_users = [{'id': user.id, 'username': user.username, 'email': user.email,
                         'password': user.password, 'phonenumber': user.phonenumber} for user in users]
    return jsonify({'users': serialized_users})





# Route to create a new user
@routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')  # Hash the password

    # Ensure required data is provided
    if 'username' not in user_data or 'email' not in user_data or 'password' not in user_data:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(email=user_data['email']).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists'}), 400

    new_user = User(
        username=user_data['username'],
        email=user_data['email'],
        phonenumber=user_data.get('phonenumber')
    )
    new_user.password = hashed_password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201




@routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    user = User.query.get(user_id)

    if user:
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.password = user_data.get('password', user.password)
        user.phonenumber = user_data.get('phonenumber', user.phonenumber)
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

# Route to partially update a user using PATCH
@routes.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    user_data = request.get_json()
    user = User.query.get(user_id)

    if user:
        if 'username' in user_data:
            user.username = user_data['username']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password = user_data['password']
        if 'phonenumber' in user_data:
            user.phonenumber = user_data['phonenumber']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})


# Similar routes for Wines
@routes.route('/wines', methods=['GET'])
def get_all_wines():
    wines = Wines.query.all()
    serialized_wines = [{'wine_id': wine.wine_id, 'name': wine.name, 'type_id': wine.type_id, 'region_id': wine.region_id, 'description': wine.description, 'varietal_id': wine.varietal_id, 'price': wine.price, 'user_rating': wine.user_rating, 'user_id': wine.user_id} for wine in wines]
    return jsonify({'wines': serialized_wines})

@routes.route('/wines', methods=['POST'])
def create_wine():
    wine_data = request.get_json()
    new_wine = Wines(
        name=wine_data.get('name'),
        type_id=wine_data.get('type_id'),
        region_id=wine_data.get('region_id'),
        description=wine_data.get('description'),
        varietal_id=wine_data.get('varietal_id'),
        price=wine_data.get('price'),
        user_rating=wine_data.get('user_rating'),
        user_id=wine_data.get('user_id')
    )
    db.session.add(new_wine)
    db.session.commit()
    return jsonify({'message': 'Wine created successfully', 'wine_id': new_wine.wine_id})



