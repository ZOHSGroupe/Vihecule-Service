from flask import jsonify
from flask import request
import models
import connection



mydb = connection.get_database()

def add_vehicle():

    args = request.json
    print(args)
    marque = args.get('marque')
    fuelType = args.get('fuelType')
    genre = args.get('genre')
    typeVihecule = args.get('typeVihecule')
    vehicleIdentificationNumber = args.get('vehicleIdentificationNumber')
    taxHorsepower = args.get('taxHorsepower')
    cylinderCount = args.get('cylinderCount')
    taxIdentificationNumber = args.get('taxIdentificationNumber')
    licensePlateNumber = args.get('licensePlateNumber')
    emptyWeight = args.get('emptyWeight')
    grossVehicleWeightRating = args.get('grossVehicleWeightRating')
    currentCarValue = args.get('currentCarValue')
    manufacturingDate = args.get('manufacturingDate')
    status = args.get('status')
    lastModificationDate = args.get('lastModificationDate')
    dateCreation = args.get('dateCreation')

    myvehicle = models.Vehicule(
        marque=marque,
        fuelType=fuelType,
        genre=genre,
        typeVihecule=typeVihecule,
        vehicleIdentificationNumber=vehicleIdentificationNumber,
        cylinderCount=cylinderCount,
        taxIdentificationNumber=taxIdentificationNumber,
        taxHorsepower=taxHorsepower,
        licensePlateNumber=licensePlateNumber,
        emptyWeight=emptyWeight,
        grossVehicleWeightRating=grossVehicleWeightRating,
        currentCarValue =currentCarValue ,
        manufacturingDate=manufacturingDate,
        status=status,
        lastModificationDate=lastModificationDate,
        dateCreation=dateCreation
        
        )
    
    myCursor = mydb.cursor()
    req = "INSERT INTO vehicles (marque, fuelType, genre, typeVihecule,vehicleIdentificationNumber,cylinderCount, taxIdentificationNumber,taxHorsepower,licensePlateNumber,emptyWeight,grossVehicleWeightRating,currentCarValue,manufacturingDate, status,lastModificationDate,dateCreation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    val = (
        myvehicle.marque, 
        myvehicle.fuelType, 
        myvehicle.genre,
        myvehicle.typeVihecule,
        myvehicle.vehicleIdentificationNumber,
        myvehicle.cylinderCount,
        myvehicle.taxIdentificationNumber,
        myvehicle.taxHorsepower, 
        myvehicle.licensePlateNumber, 
        myvehicle.emptyWeight,
        myvehicle.grossVehicleWeightRating, 
        myvehicle.currentCarValue, 
        myvehicle.manufacturingDate,
        myvehicle.status,
        myvehicle.lastModificationDate,
        myvehicle.dateCreation
    )

    myCursor.execute(req, val)
    mydb.commit()
    
    return {'status': 'save :'}
   
