from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal 


# create the class address:
class Address(BaseModel):
    
    street : str = Field(...,description="this is street")
    city : str = Field(...,description="this is city")
    state : str = Field(...,description="this is state")
    country : str = Field(...,description="this is country")
    zip_code : str = Field(...,description="this is zip code")


# create the child class.. which inherit the properties from the parent  class:
class personal_info(BaseModel):

    name : str = Field(...,description="this is name")
    age : int = Field(...,description="this is age")
    email : str = Field(...,description="this is email")
    address: Address = Field(..., description="this is address")


# create the instance of the class:
pyud_ins = personal_info(**{"name": "Muhammad zohaib khan",
                            "age": 22,
                            "email": "zohaibkhan@gmail.com",
                            "address": Address(**{"street": "123 Main St",
                                                  "city": "Nowshera",
                                                  "state": "Khyber patkhun khwa",
                                                  "country": "Pakistan",
                                                  "zip_code": "24100"
                                                  })
})


print(pyud_ins)



