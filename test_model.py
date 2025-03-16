from model.inference import predict

def test_model():
    sample_text = "I love this product!"
    expected_label = "POSITIVE"
    
    prediction = predict(sample_text)
    
    assert prediction == expected_label, f"Expected {expected_label}, but got {prediction}"

if __name__ == "__main__":
    test_model()
    print("Test passed successfully!")