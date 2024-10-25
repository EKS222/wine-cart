from datetime import datetime
from sqlalchemy.orm import validates
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates('username')
    def validate_username(self, key, username):
        if len(username) < 5:
            raise ValueError('Username must be at least 5 characters')
        return username

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email format. Must contain "@"')
        return email

    @validates('password')
    def validate_password(self, key, password):
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        return password

    @validates('phonenumber')
    def validate_phonenumber(self, key, phonenumber):
        if not str(phonenumber).isdigit() or len(str(phonenumber)) != 10:
            raise ValueError('Phone number must be exactly 10 digits')
        return phonenumber


class Wine(db.Model):
    __tablename__ = 'wines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    image = db.Columnn(db.String(100), nullable = True)
    description = db.Column(db.Text, nullable = True)
    price = db.Column(db.Float, nullable=False)
    category = db Column(db.String, nullable = False)
    rating= db.Column(db.Float, default  = 0)
    in_stock = db.Column(db Boolean, default = True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    carts = db.relationship('Cart', back_populates='wine', lazy=True)
    reviews = db.relationship('Review', backref='wine', lazy=True)
    cart_items = db.relationship('CartItem', backref='wine', lazy=True)


class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    user = db.relationship('User', back_populates='cart')
    wine = db.relationship('Wine', back_populates='carts')

    def __init__(self, user_id, wine_id, quantity=1):
        self.user_id = user_id
        self.wine_id = wine_id
        self.quantity = quantity

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating out of 5
    review_text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Review {self.rating} for Wine {self.wine_id} by User {self.user_id}>"
        

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    items = db.relationship('CartItem', backref='cart', lazy=True)

    def __repr__(self):
        return f"<Cart {self.id} for User {self.user_id}>"
        
