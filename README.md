# Introduction 
Python Application Sample for Azure

# Getting Started

To run this app locally, build the image and run the container

```bash
# Build the image
docker build -t <REGISTRY_URL>/flask-api .

# Locally run the container
docker run \
    -e "AZURE_STORAGE_CONNECTION_STRING=<STORAGE_CONNECTION_STRING>" \
    -e "AZURE_DATABASE_CONNECTION_STRING=<DATABASE_CONNECTION_STRING>" \
    <REGISTRY_URL>/flask-api
```

Then access the application at `localhost:8080`.

# Build & Push image to Container Registry
```bash
docker build -t <REGISTRY_URL>/flask-api .
docker login <REGISTRY_URL>
docker push <REGISTRY_URL>/flask-api
```