from fastapi import FastAPI
from pydantic import BaseModel
import pickle

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(client: Client):
    data = client.dict()
    prob = model.predict_proba([data])[0, 1]
    return {"probability": float(prob)}
