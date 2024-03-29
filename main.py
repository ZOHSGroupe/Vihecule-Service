from flask_app import app
from flask import jsonify
from crud.vihecule import (get_vihecules_c,create_vihecule_c,delete_vihecule_c,get_vihecule_by_id_c,
                           get_vihecules_by_client_id_c)
#from flask_jwt_extended import  jwt_required, get_jwt_identity
# Apply the @jwt_required() decorator globally
from middlewares.authJWT import verify_token

# @app.before_request
# @verify_token
# def before_request():
#     pass

@app.route('/', methods=['GET'])
def test():
    return jsonify({"message":"vehicule service work" }),200

@app.route('/vehicule', methods=['GET'])
def get_vihecules():
    return get_vihecules_c()
@app.route('/vehicule/<string:vihecule_id>', methods=['GET'])
def get_vihecule_by_id(vihecule_id:str):
    return get_vihecule_by_id_c(vihecule_id)
@app.route('/vehicule', methods=['POST'])
def create_vihecule():
    return create_vihecule_c()
@app.route('/vehicule/<string:vihecule_id>', methods=['DELETE'])
def delete_vihecule_by_id(vihecule_id):
    return delete_vihecule_c(vihecule_id)
@app.route('/vehicule/client/<string:client_id>', methods=['GET'])
def get_vihecule_by_id_client(client_id):
    return get_vihecules_by_client_id_c(client_id)



    

