from pydantic import BaseModel , Field , EmailStr , AnyUrl , field_validator ,model_validator , computed_field
from typing import List , Dict , Annotated , Optional

class Address(BaseModel):
    houseno: str
    street: str
    city: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {"houseno":"123" , "street":"Main Street" , "city":"New York"}

address1 = Address(**address_dict)

patient_dict = {"name":"John Doe" ,"gender":"Male" , "age":30 , "address":address1}
patient1 = Patient(**patient_dict)

print(patient1.address.city)