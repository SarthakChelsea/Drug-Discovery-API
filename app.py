# -*- coding: utf-8 -*-
"""
@author: Sarthak Mahapatra
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Drug import Canonical
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("regression_model.pkl","rb")
regression=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, Bioinformaticians'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Bioactivity Predictor': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_bioactivity(data:Canonical):
    data = data.smiles
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = regression.predict([[data]])
    pred=f' IC50 (in negative logarithm for better readability) value is {round(prediction[0],2)}'
    return {
        'prediction': round(prediction[0],2)
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload