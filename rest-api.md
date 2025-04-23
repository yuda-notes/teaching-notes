# REST API

## Definition
<img src="https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg"> <br>
- API (Application Programming Interface) enables different apps to communicate with each other.
- It defines the methods and data formats that applications can use to request and exchange information
- These methods consist of
  - `GET` method -> to **retrieve** data.
  - `POST` method -> to **create** new data.
  - `PUT` or `PATCH` method -> to **update** data.
  - `DELETE` method -> to **delete** data.
- API leverages HTTP protocol to allow communication between client and server.
- HTTP is a communication protocol that specifies the structure of messages between client and server.
- These messages is divided into 2 types:
  - Request -> client sends a data/message to server.
  - Response -> server returns data/message to client.
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
- To run API script we can use this command format
  ```bash
  fastapi dev [script_name.py]
  ```
- After that, we can test our API by visiting `localhost` address, usually the default is `http://localhost:8000/docs`

## More Samples
### API with CSV as Data Source
```py
# import package
from fastapi import FastAPI, HTTPException, Header
import pandas as pd

# define password for api-key auth
password = "secret123"

# create FastAPI object
app = FastAPI()

# create default endpoint
@app.get("/")
def getData(): # every endpoint must be followed with handler function
    """
    Every function must have return value in the form of JSON or Dictionary format
    """
    return {
        "message": "hello world !!!"
    }

# create another enpoint
# endpoint for showing all data from csv
@app.get("/data")
def getCsv():
    # 1. read csv using pandas
    df = pd.read_csv('data.csv')

    # 2. returns the DataFrame as dictionary
    return df.to_dict(orient="records")

# endpoint for showing specific data from csv using path-parameter
@app.get("/data/{name}") # path-params is defined inside the URL denoted with `{}`
def getDataByName(name: str): # function must also have the same parameter as the URL
    # 1. read csv
    df = pd.read_csv('data.csv')

    # 2. filter data by name
    result = df[df['name'] == name]

    # 3. validate filter result
    if len(result) > 0:
        # 4. returns response
        return result.to_dict(orient="records")
    else:
        # 5. returns error when its not valid
        raise HTTPException(status_code=404, detail="data " + name + " tidak ditemukan")

# endpoint for deleting data with api-key authentication method
@app.delete("/data/{name}")
def deleteDataByName(name: str, api_key: str = Header(None)): # the api-key is located in the header
    # check api-key
    if api_key != None and api_key == password:
        # 1. read csv
        df = pd.read_csv('data.csv')

        # 2. to delete, exclude the input name
        result = df[~(df['name'] == name)]

        # 3. replace existing csv
        result.to_csv('data.csv', index=False)

        # 4. returns response
        return {"message": "data berhasil ditambahkan"}
    else:
        # 5. returns error when api-key invalid
        raise HTTPException(status_code=403, detail="password salah!")
```

### API with Database Connection
```py
```
