import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class ClientData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

app = FastAPI()

model = joblib.load("models_and_pipelines/model.pkl")
processor = joblib.load("models_and_pipelines/processor.pkl")

@app.post("/charges")
def charges(data: ClientData):
    X = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker,
        "region": data.region
    }])

    X_prepared = processor.transform(X)
    pred = model.predict(X_prepared)[0]
    return {"charges": pred}