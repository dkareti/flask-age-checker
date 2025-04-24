#Daniel Kareti
#Created on 4/24/25

#####

#This file determines the age group of the user

#####################

import joblib

# Load pre-trained model and label encoder
try:
    model = joblib.load('model/knn_model.joblib')
    label_encoder = joblib.load('model/label_encoder.joblib')
except FileNotFoundError:
    raise RuntimeError("Model files not found. Run train_model.py first.")

def predict_age_group(age):
    encoded = model.predict([[age]])[0]
    return label_encoder.inverse_transform([encoded])[0]
