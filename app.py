from flask import Flask, request, jsonify  # Import necessary modules from Flask
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required  # Import JWT management from flask_jwt_extended
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
    try:
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

    except Exception as e:
        # Log exception and return a generic server error message
        app.logger.error(f"Login Error: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

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
    try:
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

    except Exception as e:
        # Log exception and return a generic server error message
        app.logger.error(f"Registration Error: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.route('/protected', methods=['GET'])
@jwt_required()  # Ensure the endpoint is protected and requires a valid JWT
def protected():
    """
    Access a protected route that requires authentication.

    Response:
    {
        "message": "Access granted to user <user_id>"
    }
    """
    try:
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify({"message": f"Access granted to user {current_user}"}), 200
    except Exception as e:
        # Log exception and return a generic server error message
        app.logger.error(f"Protected Route Error: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 Bad Request errors.

    Response:
    {
        "message": "Bad Request"
    }
    """
    return jsonify({"message": "Bad Request"}), 400

@app.errorhandler(401)
def unauthorized(error):
    """
    Handle 401 Unauthorized errors.

    Response:
    {
        "message": "Unauthorized"
    }
    """
    return jsonify({"message": "Unauthorized"}), 401

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 Internal Server Error errors.

    Response:
    {
        "message": "Internal Server Error"
    }
    """
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
