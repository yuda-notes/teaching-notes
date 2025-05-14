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
Link to dataset: https://raw.githubusercontent.com/yuda-notes/teaching-notes/refs/heads/main/samples/sample-fastapi-csv/dataset.csv
```py
from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
from datetime import datetime


class Profile(BaseModel):
    '''
    Profile model is used for creating request body
    '''
    name: str
    age: int
    location: str

# create FastAPI object
app = FastAPI()


@app.get("/")
async def getWelcome():
    return {
        "msg": "Sample FastAPI CSV"
    }


@app.get("/data")
async def getAllData():
    df = pd.read_csv("dataset.csv")

    return {
        "data": df.to_dict(orient="records")
    }


@app.get("/data/{location}")
async def getDataByLocation(location: str):
    df = pd.read_csv("dataset.csv")

    df = df[df.location == location]

    # validate filter data
    if len(df) > 0:
        return {
            "data": df.to_dict(orient="records")
        }

    raise HTTPException(status_code=404, detail="Data not found")


@app.patch("/data/{id}")
async def updateProfile(id: int, profile: Profile):
    df = pd.read_csv("dataset.csv")

    filter = df[df.id == id]
    # check data existence
    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    # if exists, update specific row using .loc[]
    df.loc[df.id == id, ['name', 'age', 'location']] = [
        profile.name, profile.age, profile.location]

    df.sort_values(by=['id'], ignore_index=True, inplace=True)
    df.to_csv('dataset.csv', index=False)

    return {
        "msg": "Data has been updated"
    }


@app.post("/data")
async def createProfile(profile: Profile):
    df = pd.read_csv("dataset.csv")

    newData = pd.DataFrame()
    newData['id'] = df.tail(1)['id'] + 1
    newData['name'] = profile.name
    newData['age'] = profile.age
    newData['location'] = profile.location
    newData['created_at'] = datetime.now().date()

    df = pd.concat([df, newData], ignore_index=True)

    df.sort_values(by=['id'], ignore_index=True, inplace=True)
    df.to_csv('dataset.csv', index=False)

    return {
        "data": df.tail(1).to_dict(orient='records')
    }


@app.delete('/data/{id}')
async def deleteProfile(id: int):
    df = pd.read_csv("dataset.csv")

    # check data existence
    filter = df[df.id == id]
    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    # if exists, delete it
    df = df[df.id != id]
    df.sort_values(by=['id'], ignore_index=True, inplace=True)
    df.to_csv('dataset.csv', index=False)

    return {
        "msg": "Data has been deleted"
    }
```
