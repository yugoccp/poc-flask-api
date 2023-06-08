from infra.db_client import DBClient
import sqlalchemy as db
import os

db_connection_str = os.environ.get("AZURE_DATABASE_CONNECTION_STRING ")
db_client = DBClient(db_connection_str)

def create(name):
	return "Succesfully created: " + name
	
def update(name):
	return "Succesfully updated: " + name
	
def delete(name):
	return "Succesfully deleted: " + name
	
def list():
	return db_client.connection.execute(db.select([db_client.dummy])).fetchall()