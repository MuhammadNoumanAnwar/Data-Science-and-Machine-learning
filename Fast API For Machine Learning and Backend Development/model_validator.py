from pydantic import BaseModel , EmailStr , AnyUrl , model_validator , Field 
from typing import Dict , List , Annotated , Optional

class patient(BaseModel):
    name: str
    age : int
    weight : float 
    Email : EmailStr
    Allergies : Optional[List[str]] = None
    contact : Optional[Dict[str,str]] = None

    @model_validator(mode = 'after')
    @classmethod
    def validated_emergency_contact(cls,model):
       if model.age > 60 and 'emergency' not in model.contact:
            raise ValueError("For age greater than you must procide emergency contact")
       return model

info = {'name':"npoman" , 'age':20 , 'weight':55 , 'Email':'xyz@icici.com'}

patient1 = patient(**info)