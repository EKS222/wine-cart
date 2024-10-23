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


@routes.route('/wine_types', methods=['GET'])
def get_all_wine_types():
    wine_types = WineTypes.query.all()
    serialized_wine_types = [{'type_id': wine_type.type_id, 'type_name': wine_type.type_name} for wine_type in wine_types]
    return jsonify({'wine_types': serialized_wine_types})

# Route to create a new WineType
@routes.route('/wine_types', methods=['POST'])
def create_wine_type():
    wine_type_data = request.get_json()
    new_wine_type = WineTypes(type_name=wine_type_data.get('type_name'))
    db.session.add(new_wine_type)
    db.session.commit()
    return jsonify({'message': 'WineType created successfully', 'type_id': new_wine_type.type_id})

# Similar routes for Regions
@routes.route('/regions', methods=['GET'])
def get_all_regions():
    regions = Regions.query.all()
    serialized_regions = [{'region_id': region.region_id, 'region_name': region.region_name} for region in regions]
    return jsonify({'regions': serialized_regions})

@routes.route('/regions', methods=['POST'])
def create_region():
    region_data = request.get_json()
    new_region = Regions(region_name=region_data.get('region_name'))
    db.session.add(new_region)
    db.session.commit()
    return jsonify({'message': 'Region created successfully', 'region_id': new_region.region_id})

# Similar routes for Varietals
@routes.route('/varietals', methods=['GET'])
def get_all_varietals():
    varietals = Varietals.query.all()
    serialized_varietals = [{'varietal_id': varietal.varietal_id, 'varietal_name': varietal.varietal_name, 'region_name': varietal.region_name} for varietal in varietals]
    return jsonify({'varietals': serialized_varietals})

@routes.route('/varietals', methods=['POST'])
def create_varietal():
    varietal_data = request.get_json()
    new_varietal = Varietals(varietal_name=varietal_data.get('varietal_name'), region_name=varietal_data.get('region_name'))
    db.session.add(new_varietal)
    db.session.commit()
    return jsonify({'message': 'Varietal created successfully', 'varietal_id': new_varietal.varietal_id})

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



