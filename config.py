import os  # Import os for environment variable management

class Config:
    """
    Configuration class for Flask application settings.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b131b7d8ece4c399d3949da5215a4da1b726cdcb3d9b2323baceec95863d39c1'  # Secret key for session management
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql://postgres:postgres@localhost:5432/auth_db'  # PostgreSQL connection URI
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'my_jwt_secret_key'  # Secret key for JWT signing
