## *Flask Authentication API*

This is a Flask-based RESTful API for user authentication, including login, registration, and token management. The API uses PostgreSQL for database storage and JWT for token-based authentication.

## Table of Contents: 

1. Installation
2. Configuration 
3. Endpoints  
4. Testing the API  
5. Error Handling  
6. License  


## Steps

## 1. Project Structure
![Screenshot 2024-07-29 235210](https://github.com/user-attachments/assets/f7b8ff36-9d04-4059-ab2b-af76e1385086)


## 2. clone the repository 

- git clone https://github.com/SaaaRoO/user_authentication 


## 3. Install required packages
pip install -r requirements.txt
 
 ## 4. Set up environment variables

 * export SECRET_KEY=b131b7d8ece4c399d3949da5215a4da1b726cdcb3d9b2323baceec95863d39c1
 * export DATABASE_URI=postgresql://postgres:your_password@localhost:5432/auth_db
 * export JWT_SECRET_KEY=my_jwt_secret_key

 Set up the database:

## 5. Connect to PostgreSQL and create the database

- psql -U postgres
  
![Screenshot 2024-07-29 231059](https://github.com/user-attachments/assets/1e44b188-3d97-4cca-8e16-5f7d31878045)


 - Inside the psql command-line interface:

   
 CREATE DATABASE auth_db;
\c auth_db
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


![Screenshot 2024-07-29 231335](https://github.com/user-attachments/assets/292ec6ae-6ace-4443-be65-f4a88ca48df6)


 Configuration
- The configuration for the Flask application is managed via environment variables. Update these variables to match your setup:

* SECRET_KEY: Key used for session management.
* DATABASE_URI: Connection URI for PostgreSQL.
* JWT_SECRET_KEY: Key used for signing JWT tokens.

## Endpoints

' POST /login '
- Description: Logs in a user and returns a JWT token.
![Screenshot 2024-07-30 004514](https://github.com/user-attachments/assets/1b38d488-55ae-491c-9e4e-a136bf7ce3e9)



* Request Body:
* 
{
  "username": "testuser",
  "password": "testpassword"
}

* 
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
![Screenshot 2024-07-30 003820](https://github.com/user-attachments/assets/0232be2d-ce41-44c8-9df2-4513646b30d4)



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
![Screenshot 2024-07-30 004323](https://github.com/user-attachments/assets/0fa0acb8-3aff-4d26-a44a-50aa8ec766e5)



Failure (400 Bad Request or 500 Internal Server Error):
{
  "message": "Username already exists"   // or "Registration failed"
}

## Testing the API
* Login Request:

- URL: http://127.0.0.1:5000/login
- Method: POST
- Body: (JSON with username and password)
* Headers:
- Authorization: Bearer <your_jwt_token>

- Register Request:

- URL: http://127.0.0.1:5000/register
- Method: POST
- Body: (JSON with username and password)



## Error Handling
* Invalid Credentials: Returns a 401 Unauthorized status code with a message Invalid credentials.
* Missing Parameters: Returns a 400 Bad Request status code with a message Missing parameters.
* Server Errors: Returns a 500 Internal Server Error status code with a message Registration failed.

## License
* This project is licensed under the MIT License - see the LICENSE file for details.





# user_authentication
