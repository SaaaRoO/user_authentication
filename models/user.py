from database import query_db  # Import query_db function for database interaction
from werkzeug.security import generate_password_hash, check_password_hash  # Import password hashing utilities

class User:
    """
    User class for handling user data operations.
    """
    def __init__(self, user_id, username, password):
        """
        Initialize a User instance.

        Parameters:
        - user_id: Unique identifier for the user
        - username: Username of the user
        - password: Password of the user (hashed)
        """
        self.user_id = user_id  # User ID attribute
        self.username = username  # Username attribute
        self.password = password  # Password attribute (hashed)

    @classmethod
    def find_by_username(cls, username):
        """
        Find a user by their username.

        Parameters:
        - username: Username to search for

        Returns:
        - User object if found, otherwise None
        """
        query = "SELECT * FROM users WHERE username = %s"  # SQL query to find user by username
        result = query_db(query, (username,), one=True)  # Execute query with parameter
        if result:
            # Create and return a User instance with the retrieved data
            return cls(result['user_id'], result['username'], result['password'])
        return None

    @classmethod
    def authenticate(cls, username, password):
        """
        Authenticate the user using their username and password.

        Parameters:
        - username: Username of the user
        - password: Password provided by the user

        Returns:
        - User object if authentication is successful, otherwise None
        """
        user = cls.find_by_username(username)  # Find user by username
        if user and check_password_hash(user.password, password):  # Verify password hash
            return user  # Return authenticated User object
        return None

    @staticmethod
    def create_user(username, password):
        """
        Create a new user with a hashed password.

        Parameters:
        - username: Username of the new user
        - password: Raw password to hash and store

        Returns:
        - User ID of the newly created user if successful, otherwise None
        """
        if User.find_by_username(username):  # Check if username already exists
            return None
        hashed_password = generate_password_hash(password)  # Hash the password securely
        query = "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING user_id"  # SQL query to insert new user
        result = query_db(query, (username, hashed_password), one=True)  # Execute query and get result
        if result:
            return result['user_id']  # Return newly created user ID
        return None
