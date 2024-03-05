from flask import Blueprint, request, jsonify, session
from models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
auth_blueprint = Blueprint('auth', __name__)



@auth_blueprint.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    username=data.get('username')
    password=data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username Already Exists'}),400
    hashed_password=generate_password_hash(password, method='pbkdf2:sha256')
    new_user=User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'massage': 'Registraion Successful'})


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['username'] = username
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    


@auth_blueprint.route('/logout')
def logout():
    session.pop('username', None)
    return jsonify({'message': 'Logout successful'})








