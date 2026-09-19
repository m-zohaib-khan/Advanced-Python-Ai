from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List, Literal


# create the model class:
class personal_info(BaseModel):

    name : str = Field(...,min_length=3,max_length=20,description="this is name")
    age : int | None = Field(...,ge=0, description="this is age")
    email : EmailStr = Field(...,description="this is email")
    gender : Literal["male", "female", "other"] = Field(...,description="this is gender")
    salaries : List[int] = Field(...,description="this is salaries")


# main function to print the user details:
def main(para1:personal_info):

    print("User details:")

    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salaries:", para1.salaries)


# create an instance of the model:
pyd_ins = personal_info(**{"name": "zohaib khan", "age": 25, "email": "zohaib@example.com", "gender": "male", "salaries": [5000, 6000]})

    
# call the main function with the instance of the model:
main(pyd_ins)