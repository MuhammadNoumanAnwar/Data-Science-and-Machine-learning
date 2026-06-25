from pydantic import BaseModel , EmailStr , AnyUrl , field_validator , Field 
from typing import Dict , List , Annotated , Optional

class patient(BaseModel):
    name: str
    age : int
    weight : float 
    Email : EmailStr
    Allergies : Optional[List[str]] = None

    @field_validator('Email')
    @classmethod
    def Email_validator(cls,value):
        valid = ['htfc.com','icici.com']

        domain_name = value.split('@')[-1]
        if domain_name not in valid:
            raise ValueError(f"Email domain must be one of {valid}")
        return value

info = {'name':"usman" , 'age':25 , 'weight':70.5 , 'Email':'xyz@icici.com'}

patient1 = patient(**info)