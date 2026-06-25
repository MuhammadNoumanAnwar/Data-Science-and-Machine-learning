from pydantic import BaseModel , EmailStr , AnyUrl , computed_field, Field 
from typing import Dict , List , Annotated , Optional

class patient(BaseModel):
    name: str
    age : int
    weight : float 
    Email : EmailStr
    Allergies : Optional[List[str]] = None
    contact : Optional[Dict[str,str]] = None

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.age ** 2)  # Assuming age is used as height in meters for BMI calculation
    
def print_patient_info(patient: patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.Email}")
    print(f"Allergies: {patient.Allergies}")
    print(f"Contact: {patient.contact}")
    print(f"BMI: {patient.bmi}")
    
info = {'name':"npoman" , 'age':20 , 'weight':55 , 'Email':'xyz@icici.com'}

patient1 = patient(**info)
print_patient_info(patient1)