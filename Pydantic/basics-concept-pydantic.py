# basics of pydantic:
from pydantic import BaseModel, ValidationError, Field, constr, conint, conlist, EmailStr, HttpUrl

# create the model class:
class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Name must be between 2 and 50 characters")
    age: int = Field(..., description="Age must be a positive integer")
    email: EmailStr
    website: HttpUrl

    # the three dots (...) in the Field(...) indicate that these fields are required. If you want to make a field optional, you can use None as the default value.
    # also use defualt values for the fields, like this:
    # name: str = Field("John Doe", min_length=2, max_length=50, description="Name must be between 2 and 50 characters")


# create an instance of the model:
user = User(
    name="zohaib khan",
    age=20,
    email="zohaib.khan@example.com",
    website="https://www.zohaib.com"
)


# create a function to print the user details:
def main(para1: User):

    print("User details:")

    print(para1.name)
    print(para1.age)
    print(para1.email)
    print(para1.website)


# if you want to call this function, you can need to pass the user object as an argument, like this:
main(user)
