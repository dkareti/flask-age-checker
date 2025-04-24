# train_model.py (or do this once inside ml_model.py)

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Simulated training data
data = {
    'age': [5, 8, 12, 15, 18, 22, 28, 35, 45, 55, 65, 75, 85],
    'label': ['Child', 'Child', 'Child', 'Teen', 'Teen', 'Young Adult',
              'Young Adult', 'Adult', 'Adult', 'Adult', 'Senior', 'Senior', 'Senior']
}
df = pd.DataFrame(data)

X = df[['age']]
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['label'])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, 'model/knn_model.joblib')
joblib.dump(label_encoder, 'model/label_encoder.joblib')