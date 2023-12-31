from flask_app import app
from flask import jsonify
from crud.vihecule import (get_vihecules_c,create_vihecule_c,delete_vihecule_c,get_vihecule_by_id_c,
                           get_vihecules_by_client_id_c)


##### Vihecyule
@app.route('/vihecule', methods=['GET'])
def get_vihecules():
    return get_vihecules_c()
@app.route('/vihecule', methods=['POST'])
def create_vihecule():
    return create_vihecule_c()
@app.route('/vihecule/<string:vihecule_id>', methods=['DELETE'])
def delete_vihecule_by_id(vihecule_id):
    return delete_vihecule_c(vihecule_id)
@app.route('/vihecule/client/<string:client_id>', methods=['GET'])
def get_vihecule_by_id_client(client_id):
    return get_vihecules_by_client_id_c(client_id)



    

