# REST API

## Definition
<img src="https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg"> <br>
- API (Application Programming Interface) enables different software to communicate with each other.
- It defines the methods and data formats that applications can use to request and exchange information
- These methods consist of
  - `GET` method -> to **retrieve** data.
  - `POST` method -> to **create** new data.
  - `PUT`/`PATCH` method -> to **update** data.
  - `DELETE` method -> to **delete** data.
- API leverages HTTP to allow communication between client and server.
- HTTP is a communication protocol that specifies the structure of messages exchanged between client and server.
- These messages is divided into 2 types:
  - Request -> client sends a data/message to server.
  - Response -> server returns data/mesage to client.
- This data/message is defined in **JSON** format. <br>
  <img src="https://github.com/user-attachments/assets/9f3ad44b-1d25-4bc5-9712-52947fc1632e">

## Setup
- To create an API with python, we must install **FastAPI** package. ([reference](https://fastapi.tiangolo.com/))
  ```bash
  pip install "fastapi[standard]"
  ```

## Sample API
```py
# import package
from fastapi import FastAPI

# create FastAPI object
app = FastAPI()

# create endpoint & handler
@app.get("/")
def getMain():
    return {
        "message": "Hello World",
    }
```
