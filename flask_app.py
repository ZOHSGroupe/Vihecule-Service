from flask import Flask
from flask_cors import CORS
#from flask_jwt_extended import JWTManager
import os


app = Flask(__name__)
#app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_JWT")  # Replace with your actual secret key
#app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Default is ['headers']
#jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app)