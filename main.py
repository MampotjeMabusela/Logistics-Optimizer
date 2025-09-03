from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime
import uvicorn
import logging

app = FastAPI()

class Shipment(BaseModel):
    origin: str
    destination: str
    departure_time: datetime
    cargo_type: str

@app.post("/predict_eta")
async def predict_eta(shipment: Shipment):
    # Placeholder for ML model
    eta = "2025-09-04T15:00:00"
    log_event("ETA predicted", shipment.dict())
    return {"estimated_arrival": eta}

@app.post("/parse_customs")
async def parse_customs(request: Request):
    data = await request.json()
    document_text = data.get("text", "")
    parsed = extract_customs_fields(document_text)
    log_event("Customs document parsed", parsed)
    return {"parsed_fields": parsed}

def log_event(action: str, data: dict):
    with open("audit_log.txt", "a") as f:
        f.write(f"{datetime.now()} | {action} | {data}\n")

def extract_customs_fields(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return entities

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
