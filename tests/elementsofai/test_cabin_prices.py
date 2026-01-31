from elementsofai.cabin_prices import predict

def test():
    def test_predict():
        # Test with known input and expected output
        X_test = [[66, 5, 15, 2, 500],
             [21, 3, 50, 1, 100], 
             [120, 15, 5, 2, 1200]]
        c_test = [3000, 200, -50, 5000, 100]
        expected_price = sum(x * coef for x, coef in zip(X_test[0], c_test))
        
        assert(predict(X_test, c_test) == expected_price)