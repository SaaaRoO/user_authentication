from flask import Flask, request, jsonify  # Import necessary modules from Flask
from flask_jwt_extended import JWTManager, create_access_token  # Import JWT management from flask_jwt_extended
from models.user import User  # Import User model for handling user-related operations
from config import Config  # Import configuration settings

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration settings
jwt = JWTManager(app)  # Initialize JWT Manager with Flask app

@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login by verifying credentials and issuing a JWT.

    Request:
    {
        "username": "testuser",
        "password": "testpassword"
    }

    Response:
    {
        "user_id": 1
    }

    Headers:
    {
        "Authorization": "Bearer <token>"
    }
    """
    data = request.get_json()  # Parse JSON request payload

    # Check if username and password are provided
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing parameters'}), 400

    username = data['username']
    password = data['password']

    # Authenticate user with provided credentials
    user = User.authenticate(username, password)
    if not user:
        return jsonify({'message': 'Invalid credentials'}), 401

    # Generate a JWT access token for the authenticated user
    access_token = create_access_token(identity=user.user_id)
    
    # Respond with the user_id in the body and the JWT token in the header
    response = jsonify({'user_id': user.user_id})
    response.headers['Authorization'] = f'Bearer {access_token}'
    return response, 200

@app.route('/register', methods=['POST'])
def register():
    """
    Handle new user registration by storing hashed passwords securely.

    Request:
    {
        "username": "newuser",
        "password": "newpassword"
    }

    Response:
    {
        "message": "User registered successfully",
        "user_id": 1
    }
    """
    data = request.get_json()  # Parse JSON request payload

    # Check if username and password are provided
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing parameters'}), 400

    username = data['username']
    password = data['password']

    # Check if the username already exists
    if User.find_by_username(username):
        return jsonify({'message': 'Username already exists'}), 400

    # Create a new user
    user_id = User.create_user(username, password)
    if user_id:
        return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201

    return jsonify({'message': 'Registration failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
