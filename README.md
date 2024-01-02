# Fastapi App
## Dockerize a simple python fastapi app

---

## Pull the image from the repository of dockerhub and run the fastapi app using docker command
```sh
docker pull apptimdev/fastapi
docker run -d -p 8000:8000 --name fastapi apptimdev/fastapi
```

or 

## Build the image locally and run the fastapi app using docker command
```sh
cd FastapiApp
docker build --no-cache -t apptimdev/fastapi -f Docker/Dockerfile .
docker run -d -p 8000:8000 --name fastapi apptimdev/fastapi
```

---

## Build the image locally and run the fastapi app using docker-compose command
```sh
cd FastapiApp
docker-compose build
docker-compose up -d
```

---

## Testing the application
You should be able to access the FastAPI application at http://localhost:8000
and testing the api at http://localhost:8000/docs
