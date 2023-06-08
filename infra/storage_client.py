from azure.storage.blob import BlobServiceClient


class StorageClient():

    def __init__(self, connection_str):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_str)
        

    def upload(self, container_name, blob_name, content):        
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(content, blob_type="BlockBlob")
        print("Successfully uploaded " + blob_name)


    def download(self, container_name, blob_name):
        container_client = self.blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        download_value = blob_client.download_blob().readall()
        print("Successfully downloaded " + blob_name)
        return download_value