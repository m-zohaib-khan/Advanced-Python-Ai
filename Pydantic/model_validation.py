from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Dict, Any, List, Literal


# create the model class:
class API_auth(BaseModel):

    name : str = Field(...,min_length=3,max_length=20,description="this is name")
    password : str = Field(...,min_length=8,max_length=20,description="this is password")
    confirm_password : str = Field(...,min_length=8,max_length=20,description="this is confirm password")


    # Field validator for all the model fields:
    @model_validator(mode="after") # this `After` mode is used to validate the model after all the fields have been validated.
    def password_check(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        
        else:
            return values

pyd_ins = API_auth(**{"name": "zohaib khan", "password": "password123", "confirm_password": "password123"})

print(pyd_ins)