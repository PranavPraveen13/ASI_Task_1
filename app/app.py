import streamlit as st
from predict import predict

st.title("Iris Flower Prediction App")
st.write("Enter the flower's measurements below to predict its species.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict"):
    features = [sepal_length, sepal_width, petal_length, petal_width]
    result = predict(features)
    st.success(f"The predicted Iris species is: {result}")

