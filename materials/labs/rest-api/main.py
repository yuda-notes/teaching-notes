# import packages
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# create FastAPI object
app = FastAPI()


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
        "msg": "Hello world!"
    }


@app.get('/profiles')
def getProfiles():
    '''
    endpoint 2 - get all profiles
    '''

    # complete this endpoint
    pass


@app.get('/profiles/{id}')
def getProfile(id: int):
    '''
    endpoint 2 - get profile by id
    '''

    # complete this endpoint
    pass


@app.delete('/profiles/{id}')
def deleteProfile(id: int):
    '''
    endpoint 3 - delete profile by id
    '''

    # complete this endpoint
    pass


@app.put('/profiles/{id}')
def updateProfile(id: int, profile: Profile):
    '''
    endpoint 4 - update profile by id
    '''

    # complete this endpoint
    pass


@app.post('/profiles/')
def createProfile(profile: Profile):
    '''
    endpoint 5 - create new profile
    '''

    # complete this endpoint
    pass
