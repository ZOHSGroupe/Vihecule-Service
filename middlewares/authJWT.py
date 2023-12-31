from flask import jsonify,request
from functools import wraps
import jwt  # Import the PyJWT library
import os

def verify_token(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify(message='No token provided!'), 403

        try:
            # Replace 'your_secret_key' with your actual secret key
            decoded = jwt.decode(token, os.getenv("SECRET_JWT"), algorithms=['HS256'])
            # You can access user_id using decoded['sub'] or any other claim you set
            # request.user_id = decoded['sub']
        except jwt.ExpiredSignatureError:
            return jsonify(message='Token has expired'), 401
        except jwt.InvalidTokenError:
            return jsonify(message='Invalid token'), 401

        return fn(*args, **kwargs)

    return wrapper