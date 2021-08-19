from sqlalchemy import create_engine
from Database.models import Base
from sqlalchemy.orm import sessionmaker



#File path for the locaiton of the database
URI = "sqlite:////media/shafiq/New Volume/Dropbox/Cognism-Proj/Cognism-Project/Database/cognism_db.sqlite"
sqlite_db_uri = URI

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
