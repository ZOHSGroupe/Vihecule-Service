from database.database import db
from sqlalchemy import Column, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

#Base = declarative_base()
class Client(db.Model):
    __tablename__ = 'client'
    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    national_id = Column(String)
    email = Column(String)
    city = Column(String)
    birth_date = Column(Date)
    nationality = Column(String)
    gender = Column(String)
    create_date = Column(Date, default=datetime.utcnow)
    address = Column(String)
    status = Column(String)