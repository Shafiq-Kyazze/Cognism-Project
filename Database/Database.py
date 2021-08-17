from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker



#File path for the locaiton of the database
sqlite_db_uri = "sqlite:///cognism_db.sqlite"

#connecting database to SQLALCHEMY
engine = create_engine(sqlite_db_uri)

#Binding SQL alchemy's ORM to the sqlite database  database
Session = sessionmaker(bind=engine)
s = Session() #Session allows us to make queries on the database

#Creating tables
Base.metadata.create_all(engine)

#Uploading changes
s.commit()

#CLosing session
s.close()
