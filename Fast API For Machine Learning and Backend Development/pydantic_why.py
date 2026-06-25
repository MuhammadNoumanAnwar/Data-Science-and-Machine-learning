from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List, Dict , Optional ,Annotated
class Patient(BaseModel):
    name:  Annotated[str, Field(min_length=1,title = "Patient Name", examples = ["John Doe"],max_length=50)]
    age : int = Field(gt=0,le=120)
    email : EmailStr
    linkedin_url: AnyUrl
    weight : Annotated[float,Field(gt=0,le=300,strict=True,description="Weight in kg")]
    married : bool
    allergies : Optional[List[str]] = Field(default=None, max_length=10)
    contact_details : Dict[str,str]

def insert_patient(patient: Patient):
        pass    

patient_info = {"name":'usman' , "age":25 , "email":"usman@example.com" ,"linkedin_url":"https://linkedin.com/in/usman" , "weight":70.5 , "married":False , "allergies":['dust','pollen'] , "contact_details":{"phone":"1234567890"}}
patientp1 = Patient(**patient_info)