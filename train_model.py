# train_model.py (or do this once inside ml_model.py)

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from enum import Enum
import random

'''
GENERATE THE SPECIFIED DATA FROM THE NUMBER OF SAMPLES
'''
NUM_SAMPLES = 100

class AgeLabel(Enum):
    CHILD = 'Child'
    TEEN = 'Teen'
    YOUNG_ADULT = 'Young Adult'
    ADULT = 'Adult'
    SENIOR = 'Senior'
    DEAD = 'Dead'

def classify_age(age: int) -> AgeLabel:
    if(age < 13):
        return AgeLabel.CHILD
    elif(age < 20):
        return AgeLabel.TEEN
    elif(age < 27):
        return AgeLabel.YOUNG_ADULT
    elif(age < 69):
        return AgeLabel.ADULT
    elif(age < 97):
        return AgeLabel.SENIOR
    else:
        return AgeLabel.DEAD
    
def generate_data(n_samples=NUM_SAMPLES) -> dict:
    data = {'age': [], 'label' : []}

    for _ in range(n_samples):
        age = random.randint(0, 100)
        label = classify_age(age).value
        data['age'].append(age)
        data['label'].append(label)
    
    return data

# Simulated training data
data = generate_data()
df = pd.DataFrame(data)

X = df[['age']]
'''
The line above produces a 2D matrix
'''
label_encoder = LabelEncoder() #converts the labels into numerical values
y = label_encoder.fit_transform(df['label'])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, 'model/knn_model.joblib')
joblib.dump(label_encoder, 'model/label_encoder.joblib')