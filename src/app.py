import os
import pickle

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from bank_note import BankNote

# Load model path from env
load_dotenv()

# Create the app object
app = FastAPI()
pickle_in = open(os.environ.get("MODEL_PATH"), "rb")
classifier = pickle.load(pickle_in)


@app.get("/")
def index():
    """
    Index route -> http://127.0.0.1:8000
    """
    return {"message": "Hello, World"}


@app.get("/{name}")
def get_name(name: str):
    """
    Route with a single parameter, returns the parameter within a message
    URL Parameter route -> http://127.0.0.1:8000/AnyNameHere
    """
    return {"Welcome To Second page": f"{name}"}


@app.post("/predict")
def predict_banknote(data: BankNote):
    """
    Exposes the prediction data, make a prediction from the passed
    JSON data and return the predicted Bank Note with the confidence
    """
    # converts pydentic model to dict
    data = data.model_dump()
    # extract values from dict
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    # invoke predict with extracted feature values
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    # The predicted value is from a random forest classifier
    # So we need to check further condition for final output
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Its a Bank note"
    return {"prediction": prediction}


if __name__ == "__main__":
    """
    Run the API with uvicorn
    Will run on http://127.0.0.1:8000
    """
    uvicorn.run(app, host="127.0.0.1", port=8000)
