from flask import jsonify, request, Blueprint
from .models import db, User, Wine, Cart, CartItem, Review
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

    if not all(key in user_data for key in ('username', 'email', 'password')):
        return jsonify({'message': 'Username, email, and password are required'}), 400

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
            'rating': wine.rating,
            'in_stock': wine.in_stock,
            'image_url': wine.image_url,
            'category': wine.category
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
        price=wine_data['price'],
        category=wine_data.get('category'),
        in_stock=wine_data.get('in_stock', True),
        image_url=wine_data.get('image_url')
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
        wine.category = wine_data.get('category', wine.category)
        wine.in_stock = wine_data.get('in_stock', wine.in_stock)
        wine.image_url = wine_data.get('image_url', wine.image_url)
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
    cart = Cart.query.filter_by(user_id=user_id).first()

    if not cart:
        return jsonify({'message': 'Cart not found'}), 404

    serialized_cart = [
        {
            'id': item.id,
            'wine_id': item.wine_id,
            'quantity': item.quantity
        }
        for item in cart.items
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

    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()

    cart_item = CartItem.query.filter_by(cart_id=cart.id, wine_id=wine_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, wine_id=wine_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({'message': 'Wine added to cart'}), 201


# Update cart item quantity
@routes.route('/cart/<int:cart_item_id>', methods=['PUT'])
@jwt_required()
def update_cart_item(cart_item_id):
    cart_data = request.get_json()
    cart_item = CartItem.query.get(cart_item_id)

    if cart_item and cart_item.cart.user_id == get_jwt_identity():
        cart_item.quantity = cart_data.get('quantity', cart_item.quantity)
        db.session.commit()
        return jsonify({'message': 'Cart item updated successfully'}), 200
    return jsonify({'message': 'Cart item not found or unauthorized'}), 404


# Delete item from cart
@routes.route('/cart/<int:cart_item_id>', methods=['DELETE'])
@jwt_required()
def delete_cart_item(cart_item_id):
    cart_item = CartItem.query.get(cart_item_id)
    if cart_item and cart_item.cart.user_id == get_jwt_identity():
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({'message': 'Cart item deleted successfully'}), 200
    return jsonify({'message': 'Cart item not found or unauthorized'}), 404


# -------------------------
# Review CRUD Operations
# -------------------------

# Get all reviews for a wine
@routes.route('/wines/<int:wine_id>/reviews', methods=['GET'])
def get_reviews(wine_id):
    reviews = Review.query.filter_by(wine_id=wine_id).all()
    serialized_reviews = [
        {
            'id': review.id,
            'user_id': review.user_id,
            'rating': review.rating,
            'review_text': review.review_text
        }
        for review in reviews
    ]
    return jsonify({'reviews': serialized_reviews}), 200


# Add a review for a wine
@routes.route('/wines/<int:wine_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(wine_id):
    review_data = request.get_json()
    new_review = Review(
        wine_id=wine_id,
        user_id=get_jwt_identity(),
        rating=review_data['rating'],
        review_text=review_data.get('review_text')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully', 'review_id': new_review.id}), 201


# Update a review
@routes.route('/reviews/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    review_data = request.get_json()
    review = Review.query.get(review_id)

    if review and review.user_id == get_jwt_identity():
        review.rating = review_data.get('rating', review.rating)
        review.review_text = review_data.get('review_text', review.review_text)
        db.session.commit()
        return jsonify({'message': 'Review updated successfully'}), 200
    return jsonify({'message': 'Review not found or unauthorized'}), 404


# Delete a review
@routes.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    review = Review.query.get(review_id)
    if review and review.user_id == get_jwt_identity():
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully'}), 200
    return jsonify({'message': 'Review not found or unauthorized'}), 404
    
