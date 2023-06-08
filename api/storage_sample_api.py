from infra.storage_client import StorageClient
from datetime import datetime
import os

storage_connection_str = os.environ.get("AZURE_STORAGE_CONNECTION_STRING ")
container_name = "helloflaskcontainer"
storage_client = StorageClient(storage_connection_str)

def upload(filename):
	storage_client.upload(container_name, filename, datetime.now() + ": some new content...")
	return "Succesfully uploaded!"

def download(filename):
	download_value = storage_client.download(container_name, str(filename))
	return "Succesfully donwloaded: " + download_value