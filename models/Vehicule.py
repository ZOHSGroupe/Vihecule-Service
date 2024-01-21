from database.database import db
from sqlalchemy import Column, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models.client import Client
#Base = declarative_base()
class Vehicule(db.Model):
    __tablename__ = 'vehicule'

    id = Column(String, primary_key=True)
    marque = Column(String)
    genre = Column(String)
    type_vehicle = Column(String)
    fuel_type = Column(String)
    vehicle_identification_number = Column(String)
    cylinder_count = Column(String)
    tax_identification_number = Column(String)
    tax_horsepower = Column(String)
    license_plate_number = Column(String)
    empty_weight = Column(Float)
    gross_vehicle_weight_rating = Column(Float)
    current_car_value = Column(Float)
    manufacturing_date = Column(Date)
    status = Column(String)
    date_creation = Column(Date, default=datetime.utcnow)

    client_id = Column(String, ForeignKey('client.id'))
    client = relationship('Client')

    #assurance = relationship('Assurance', back_populates='vihecule', uselist=False, cascade='all, delete-orphan')
    #contrat = relationship('Contrat', back_populates='vihecule', uselist=False, cascade='all, delete-orphan')
    #link_list = relationship('Link', back_populates='vihecule', cascade='all, delete-orphan')

