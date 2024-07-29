## *Flask Authentication API*

This is a Flask-based RESTful API for user authentication, including login, registration, and token management. The API uses PostgreSQL for database storage and JWT for token-based authentication.

##Table of Contents: ##

1.Installation
2.Configuration 
3.Endpoints  
4.Testing the API  
5.Error Handling  
6.License  


## Steps
## clone the repository 

git clone https://github.com/SaaaRoO/user_authentication /n
cd user_authentication

## Install required packages
pip install -r requirements.txt
 
 ## Set up environment variables

 export SECRET_KEY=b131b7d8ece4c399d3949da5215a4da1b726cdcb3d9b2323baceec95863d39c1
 export DATABASE_URI=postgresql://postgres:your_password@localhost:5432/auth_db
 export JWT_SECRET_KEY=my_jwt_secret_key

 Set up the database:

## Connect to PostgreSQL and create the database

psql -U postgres
 
 - Inside the psql command-line interface:
 CREATE DATABASE auth_db;
\c auth_db
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
 Configuration
- The configuration for the Flask application is managed via environment variables. Update these variables to match your setup:

* SECRET_KEY: Key used for session management.
* DATABASE_URI: Connection URI for PostgreSQL.
* JWT_SECRET_KEY: Key used for signing JWT tokens.

## Endpoints

' POST /login '
Description: Logs in a user and returns a JWT token.

* Request Body:
{
  "username": "testuser",
  "password": "testpassword"
}

* Response :
{
  "user_id": 1
}
 
* Header:
Authorization: Bearer <your_jwt_token>
 
* Failure (400 Bad Request or 401 Unauthorized):

 {
  "message": "Invalid credentials"   // or "Missing parameters"
}

' POST /register ' 
Description: Registers a new user.

* Request Body:
{
  "username": "newuser",
  "password": "newpassword"
}

Response:

Success (201 Created):
{
  "message": "User registered successfully",
  "user_id": 1
}

Failure (400 Bad Request or 500 Internal Server Error):
{
  "message": "Username already exists"   // or "Registration failed"
}

## Testing the API
* Login Request:

URL: http://127.0.0.1:5000/login
Method: POST
Body: (JSON with username and password)
* Headers:
Authorization: Bearer <your_jwt_token>

- Register Request:

URL: http://127.0.0.1:5000/register
Method: POST
Body: (JSON with username and password)

- Protected Endpoint Request:

URL: http://127.0.0.1:5000/protected 
Method: GET or POST
Headers:
Authorization: Bearer <your_jwt_token>

## Error Handling
* Invalid Credentials: Returns a 401 Unauthorized status code with a message Invalid credentials.
* Missing Parameters: Returns a 400 Bad Request status code with a message Missing parameters.
* Server Errors: Returns a 500 Internal Server Error status code with a message Registration failed.

License
This project is licensed under the MIT License - see the LICENSE file for details.





# user_authentication
