import joblib
import numpy as np

# Load model
model = joblib.load("app/model.joblib")

def predict(features):

    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]

    species = ["Setosa", "Versicolor", "Virginica"]
    return species[prediction]
