from models.Vehicule import Vehicule
from models.client import Client
from flask import jsonify, request
from database.database import db 
import uuid

def get_vihecules_c():
    try:
        # Query all Vihecules from the database
        vihecules = Vehicule.query.all()

        # Convert Vihecules to a list of dictionaries
        vihecules_data = []
        for vehicule in vihecules:
            vihecule_data = {
                'id':vehicule.id,
                'marque': vehicule.marque,
                'genre': vehicule.genre,
                'typetype_vehicle':vehicule.type_vehicle,
                'fuelType': vehicule.fuel_type,
                'vehicleIdentificationNumber': vehicule.vehicle_identification_number,
                'cylinderCount': vehicule.cylinder_count,
                'taxIdentificationNumber':vehicule.tax_identification_number,
                'taxHorsepower': vehicule.tax_horsepower,
                'licensePlateNumber':vehicule.license_plate_number,
                'emptyWeight': vehicule.empty_weight,
                'grossVehicleWeightRating': vehicule.gross_vehicle_weight_rating,
                'currentCarValue': vehicule.current_car_value,
                'manufacturingDate': vehicule.manufacturing_date.isoformat() if vehicule.manufacturing_date else None,
                'status': vehicule.status,
                'dateCreation': vehicule.date_creation.isoformat() if vehicule.date_creation else None,
                'client_id':vehicule.client_id
                # Include other fields as needed
            }
            vihecules_data.append(vihecule_data)

        return jsonify(vihecules_data), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error

def create_vihecule_c():
    try:
        # Get data from the request payload
        data = request.get_json()
        
        id_=str(uuid.uuid4())
        # Check if the client exists
        client_id = data.get('client_id')
        client = Client.query.get(client_id)
        if client is None:
            return jsonify({"message":f"Client with ID {client_id} not found"}),404
        # Create a new Vihecule instance
        new_vihecule = Vehicule(
            id=id_,
            marque=data.get('marque'),
            genre=data.get('genre'),
            type_vehicle =data.get('typevehicle'),
            fuel_type=data.get('fuelType'),
            vehicle_identification_number=data.get('vehicleIdentificationNumber'),
            cylinder_count=data.get('cylinderCount'),
            tax_identification_number=data.get('taxIdentificationNumber'),
            tax_horsepower=data.get('taxHorsepower'),
            license_plate_number=data.get('licensePlateNumber'),
            empty_weight=data.get('emptyWeight'),
            gross_vehicle_weight_rating=data.get('grossVehicleWeightRating'),
            current_car_value=data.get('currentCarValue'),
            manufacturing_date=data.get('manufacturingDate'),
            status=data.get('status'),
            client_id=client_id
        )

        # Add the new Vihecule to the database
        db.session.add(new_vihecule)
        db.session.commit()

        return jsonify({"message":f"vihecule added successufully with id {id_}"}), 201  # 201 Created

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error

def delete_vihecule_c(vihecule_id):
    try:
        # Find the Vihecule by ID
        vihecule = Vehicule.query.get(vihecule_id)
        if vihecule is None:
            return jsonify({'message': f'Vihecule not found with id : {vihecule_id} '}), 404  # 404 NOT FOUND
        # Delete the Vihecule from the database
        db.session.delete(vihecule)
        db.session.commit()

        return jsonify({'message': 'Vihecule deleted successfully'}), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error


def get_vihecule_by_id_c(vihecule_id):
    try:
        # Find the Vihecule by ID
        Vehicule = Vehicule.query.get(vihecule_id)
        if  Vehicule is None:
            return jsonify({'message': f'Vihecule not found with id : {vihecule_id} '}), 404  # 404 NOT FOUND
        # Convert Vihecule to a dictionary
        vihecule_data = {
            'id': Vehicule.id,
            'marque': Vehicule.marque,
            'genre': Vehicule.genre,
            'typevehicle': Vehicule.type_vehicle,
            'fuelType': Vehicule.fuel_type,
            'vehicleIdentificationNumber': Vehicule.vehicle_identification_number,
            'cylinderCount': Vehicule.cylinder_count,
            'taxIdentificationNumber': Vehicule.tax_identification_number,
            'taxHorsepower': Vehicule.tax_horsepower,
            'licensePlateNumber': Vehicule.license_plate_number,
            'emptyWeight': Vehicule.empty_weight,
            'grossVehicleWeightRating': Vehicule.gross_vehicle_weight_rating,
            'currentCarValue': Vehicule.current_car_value,
            'manufacturingDate': Vehicule.manufacturing_date.isoformat() if Vehicule.manufacturing_date else None,
            'status': Vehicule.status,
            'dateCreation': Vehicule.date_creation.isoformat() if Vehicule.date_creation else None,
            'client_id':Vehicule.client_id
        }

        return jsonify(vihecule_data), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error


def get_vihecules_by_client_id_c(client_id):
    try:
        # Query all Vihecules from the database
        vihecules = Vehicule.query.all()

        # Convert Vihecules to a list of dictionaries
        vihecules_data = []
        for Vehicule in vihecules:
            if Vehicule.client_id==client_id:
                vihecule_data = {
                    'id': Vehicule.id,
                    'marque': Vehicule.marque,
                    'genre': Vehicule.genre,
                    'typevehicle': Vehicule.type_vehicle,
                    'fuelType': Vehicule.fuel_type,
                    'vehicleIdentificationNumber': Vehicule.vehicle_identification_number,
                    'cylinderCount': Vehicule.cylinder_count,
                    'taxIdentificationNumber': Vehicule.tax_identification_number,
                    'taxHorsepower': Vehicule.tax_horsepower,
                    'licensePlateNumber': Vehicule.license_plate_number,
                    'emptyWeight': Vehicule.empty_weight,
                    'grossVehicleWeightRating': Vehicule.gross_vehicle_weight_rating,
                    'currentCarValue': Vehicule.current_car_value,
                    'manufacturingDate': Vehicule.manufacturing_date.isoformat() if Vehicule.manufacturing_date else None,
                    'status': Vehicule.status,
                    'dateCreation': Vehicule.date_creation.isoformat() if Vehicule.date_creation else None,
                    'client_id':Vehicule.client_id
                    # Include other fields as needed
                }
                vihecules_data.append(vihecule_data)
        return jsonify(vihecules_data), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error