# import packages
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import pandas as pd

# postgres -> psycopg2 atau SQL Alchemy

# create FastAPI object
app = FastAPI()

# password - api key
password = "kopiluwakgabikinkenyang2000"


class Profile(BaseModel):
    '''
    Profile class - used for making request body
    '''
    name: str
    location: str


@app.get('/')
def getHome():
    '''
    endpoint 1 - home page
    '''

    return {
        "msg": "Hello world"
    }


@app.get('/profiles')
def getProfiles():
    '''
    endpoint 2 - get all profiles
    '''

    # membaca isi datasource
    df = pd.read_csv('dataset.csv')

    return {
        "data": df.to_dict(orient='records')
    }


# path/url parameter
@app.get('/profiles/{id}')
def getProfile(id: int):
    '''
    endpoint 3 - get profile by id
    '''

    # membaca isi datasource
    df = pd.read_csv('dataset.csv')

    # filter data sesuai id
    result = df.query(f"id == {id}")

    # ketika result kosong -> pesan error
    if len(result) == 0:
        # tampilkan error -> raise
        raise HTTPException(status_code=404, detail="data not found!")

    # ketika tidak kosong
    return {
        "data": result.to_dict(orient='records')
    }


@app.delete('/profiles/{id}')
def deleteProfile(id: int, api_key: str = Header(None)):
    '''
    endpoint 4 - delete profile by id
    '''

    # cek password
    if (api_key == None) or (api_key != password):
        # raise error
        raise HTTPException(status_code=401, detail="Unauthorized access!")

    # membaca isi datasource
    df = pd.read_csv('dataset.csv')

    # filter - exclude id yang bersangkutan
    result = df.query(f"id != {id}")

    # replace dataset dengan yang baru
    result.to_csv('dataset.csv', index=False)

    return {
        "data": result.to_dict(orient='records')
    }


@app.put('/profiles/{id}')
def updateProfile(id: int, profile: Profile):
    '''
    endpoint 5 - update profile by id
    '''

    # complete this endpoint
    pass


@app.post('/profiles')
def createProfile(profile: Profile):
    '''
    endpoint 6 - create new profile
    '''

    # membaca isi datasource
    df = pd.read_csv('dataset.csv')

    # buat data baru
    newDf = pd.DataFrame({
        "id": [len(df) + 1],
        "name": [profile.name],
        "location": [profile.location]
    })

    # concat
    df = pd.concat([df, newDf])

    # replace dataset existing
    df.to_csv('dataset.csv', index=False)

    return {
        "msg": "Data has created successfully!"
    }
