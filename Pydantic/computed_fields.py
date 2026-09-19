# computer fields are used to compute the value of a field based on the values of other fields in the model. They are defined using the @computed_field decorator, which takes a function that computes the value of the field based on the values of other fields in the model.
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import Optional, Dict, Any, List, Literal


# create the model class:
class orders(BaseModel):
    id : int = Field(...,description="this is id")
    unit_price : float = Field(...,description="this is unit price")
    quantity : int = Field(...,description="this is quantity")
    amount : float = Field(...,description="this is amount")


    # computed field for amount
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.unit_price * self.quantity



# create an instance of the model:
pyd_ins = orders(**{"id": 1, "unit_price": 10.5, "quantity": 5, "amount": 0})

print(pyd_ins)

    