# my-quart-api

This project is a simple example of a REST API using the Quart framework.

## Build whl package
```bash
bash packageLocally.sh
```

## Build Docker image
```bash
docker build -t my-quart-api .
```

## Run
```bash 
docker run -p 10002:10002 --network=host my-quart-api
```

## Access to Swagger
http://localhost:10002/


