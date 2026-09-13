from fastapi import FastAPI
from pydantic import BaseModel
# more protected method to pass the data to my api 
class Input(BaseModel):
    age : int
    sex : str
    
app = FastAPI()
@app.get("/predict")
def predict_model(age: int, sex: str):
    # a demo code below
    if age < 15 or sex == 'F':
        return {'survived' : 1}

    else:
        return {'survived':0}