from flask import jsonify
from datetime import datetime
from enum import Enum


class TypeVihecule(Enum):
    CAR = "CAR"
    TRUCK = "TRUCK"
    MOTORCYCLE = "MOTORCYCLE"
    BUS = "BUS"
    VAN = "VAN"
    ELECTRIC_SCOOTER = "ELECTRIC_SCOOTER"
    BOAT = "BOAT"
    AIRPLANE = "AIRPLANE"
    HELICOPTER = "HELICOPTER"
    BICYCLE = "BICYCLE"
    ELECTRIC_CAR = "ELECTRIC_CAR"
    ELECTRIC_BICYCLE = "ELECTRIC_BICYCLE"
    ELECTRIC_BUS = "ELECTRIC_BUS"
    ELECTRIC_TRUCK = "ELECTRIC_TRUCK"
    HYBRID_CAR = "HYBRID_CAR"
    HYBRID_BUS = "HYBRID_BUS"
    HYBRID_TRUCK = "HYBRID_TRUCK"
    SCOOTER = "SCOOTER"
    SUBMARINE = "SUBMARINE"
    AIRSHIP = "AIRSHIP"
    GO_KART = "GO_KART"
    SEGWAY = "SEGWAY"
   

class FuelType(Enum):
    PETROL = "PETROL"
    DIESEL = "DIESEL"

class Status(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"





class Vehicule:
    def __init__(self, data):
        self.id = data['id']
        self.marque = data['marque']
        self.genre = data['genre']
        self.typeVihecule = TypeVihecule[data['typeVihecule']]
        self.fuelType = FuelType[data['fuelType']]
        self.vehicleIdentificationNumber = data['vehicleIdentificationNumber']
        self.cylinderCount = data['cylinderCount']
        self.taxIdentificationNumber = data['taxIdentificationNumber']
        self.taxHorsepower = data['taxHorsepower']
        self.licensePlateNumber = data['licensePlateNumber']
        self.emptyWeight = data['emptyWeight']
        self.grossVehicleWeightRating = data['grossVehicleWeightRating']
        self.currentCarValue = data['currentCarValue']
        self.manufacturingDate = datetime.strptime(data['manufacturingDate'], '%Y-%m-%d')
        self.status = Status[data['status']]
        self.lastModificationDate = datetime.strptime(data['lastModificationDate'], '%Y-%m-%d')
        self.dateCreation = datetime.now()

def jsonify_vehicle(vehicle_list):
    return jsonify({'vehicle': vehicle_list})