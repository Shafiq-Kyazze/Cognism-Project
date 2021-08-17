"""Data models to construct the tables for the 3 files"""
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

#To be used to construct the data models by SQL ALCHEMY
Base = declarative_base()

""" Data Model for companies file"""
class COMPANIES(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String, nullable=True) #Column won't be null


"""Model for location file"""
class LOCATION(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String, nullable=True)
    location_type = Column(String, nullable=True)

"""Model for legal file"""
class LEGAL(Base):
    __tablename__ = 'legal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    legal_term = Column(String, nullable=False)