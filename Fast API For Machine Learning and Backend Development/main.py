from fastapi import FastAPI , Path , HTTPException , Query
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f);
    
    return data

@app.get("/")
def hello():
    return {"message": "Hello world"}

@app.get("/about")
def about():
    return {"message":"Starting fast api"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patients/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "ID of the patient to view" , example = "P101")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise  HTTPException(status_code = 404 , detail = "patient not found")
    