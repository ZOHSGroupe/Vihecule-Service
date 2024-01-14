from models.vihecule import Vihecule
from models.client import Client
from flask import jsonify, request
from database.database import db 
import uuid

def get_vihecules_c():
    try:
        # Query all Vihecules from the database
        vihecules = Vihecule.query.all()

        # Convert Vihecules to a list of dictionaries
        vihecules_data = []
        for vihecule in vihecules:
            vihecule_data = {
                'id': vihecule.id,
                'marque': vihecule.marque,
                'genre': vihecule.genre,
                'typeVihecule': vihecule.type_vihecule,
                'fuelType': vihecule.fuel_type,
                'vehicleIdentificationNumber': vihecule.vehicle_identification_number,
                'cylinderCount': vihecule.cylinder_count,
                'taxIdentificationNumber': vihecule.tax_identification_number,
                'taxHorsepower': vihecule.tax_horsepower,
                'licensePlateNumber': vihecule.license_plate_number,
                'emptyWeight': vihecule.empty_weight,
                'grossVehicleWeightRating': vihecule.gross_vehicle_weight_rating,
                'currentCarValue': vihecule.current_car_value,
                'manufacturingDate': vihecule.manufacturing_date.isoformat() if vihecule.manufacturing_date else None,
                'status': vihecule.status,
                'numberOfPorts':vihecule.number_of_ports,
                'dateCreation': vihecule.date_creation.isoformat() if vihecule.date_creation else None,
                'client_id':vihecule.client_id
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
        new_vihecule = Vihecule(
            id=id_,
            marque=data.get('marque'),
            genre=data.get('genre'),
            type_vihecule=data.get('typeVihecule'),
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
        vihecule = Vihecule.query.get(vihecule_id)
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
        vihecule = Vihecule.query.get(vihecule_id)
        if vihecule is None:
            return jsonify({'message': f'Vihecule not found with id : {vihecule_id} '}), 404  # 404 NOT FOUND
        # Convert Vihecule to a dictionary
        vihecule_data = {
            'id': vihecule.id,
            'marque': vihecule.marque,
            'genre': vihecule.genre,
            'typeVihecule': vihecule.type_vihecule,
            'fuelType': vihecule.fuel_type,
            'vehicleIdentificationNumber': vihecule.vehicle_identification_number,
            'cylinderCount': vihecule.cylinder_count,
            'taxIdentificationNumber': vihecule.tax_identification_number,
            'taxHorsepower': vihecule.tax_horsepower,
            'licensePlateNumber': vihecule.license_plate_number,
            'emptyWeight': vihecule.empty_weight,
            'grossVehicleWeightRating': vihecule.gross_vehicle_weight_rating,
            'currentCarValue': vihecule.current_car_value,
            'manufacturingDate': vihecule.manufacturing_date.isoformat() if vihecule.manufacturing_date else None,
            'status': vihecule.status,
            'dateCreation': vihecule.date_creation.isoformat() if vihecule.date_creation else None,
            'client_id':vihecule.client_id
        }

        return jsonify(vihecule_data), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error


def get_vihecules_by_client_id_c(client_id):
    try:
        # Query all Vihecules from the database
        vihecules = Vihecule.query.all()

        # Convert Vihecules to a list of dictionaries
        vihecules_data = []
        for vihecule in vihecules:
            if vihecule.client_id==client_id:
                vihecule_data = {
                    'id': vihecule.id,
                    'marque': vihecule.marque,
                    'genre': vihecule.genre,
                    'typeVihecule': vihecule.type_vihecule,
                    'fuelType': vihecule.fuel_type,
                    'vehicleIdentificationNumber': vihecule.vehicle_identification_number,
                    'cylinderCount': vihecule.cylinder_count,
                    'taxIdentificationNumber': vihecule.tax_identification_number,
                    'taxHorsepower': vihecule.tax_horsepower,
                    'licensePlateNumber': vihecule.license_plate_number,
                    'emptyWeight': vihecule.empty_weight,
                    'grossVehicleWeightRating': vihecule.gross_vehicle_weight_rating,
                    'currentCarValue': vihecule.current_car_value,
                    'manufacturingDate': vihecule.manufacturing_date.isoformat() if vihecule.manufacturing_date else None,
                    'status': vihecule.status,
                    'dateCreation': vihecule.date_creation.isoformat() if vihecule.date_creation else None,
                    'client_id':vihecule.client_id
                    # Include other fields as needed
                }
                vihecules_data.append(vihecule_data)
        return jsonify(vihecules_data), 200  # 200 OK

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error