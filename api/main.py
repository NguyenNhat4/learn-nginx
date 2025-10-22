from fastapi import FastAPI
from loguru import logger
import os


# Getting environment variables
model_id = os.environ.get('MODEL_ID')


# Creating FastAPI instance
app = FastAPI(root_path="/service{}".format(model_id))

# Build the APIs
@app.post("/predict")
def predict():
    # Predicting the class
    logger.info("Model ID {} completed prediction!".format(model_id))

    # Return the result
    return {"pred": 1}


