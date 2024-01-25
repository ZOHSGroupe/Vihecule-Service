from flask import Flask
from flask_cors import CORS
#from flask_jwt_extended import JWTManager
import os
from pyeureka import PyEureka


app = Flask(__name__)
#app.config['JWT_SECRET_KEY'] = os.getenv("SECRET_JWT")  # Replace with your actual secret key
#app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Default is ['headers']
#jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app)

eureka = PyEureka(
    app,
    eureka_server="http://localhost:8761/eureka/",
    app_name="Vihecule-service", 
)
if __name__ == "__main__":
    eureka.register()
    app.run(port=5000)