from app.predict import predict

def test_predict_valid():
    features = [5.1, 3.5, 1.4, 0.2]
    result = predict(features)
    assert result in ["Setosa", "Versicolor", "Virginica"]
