import unittest
from app import app

class FlaskTest(unittest.TestCase):

       # Ensure that the predict route returns the expected prediction
    def test_predict_output(self):
        tester = app.test_client(self)
        response = tester.post('/predict', data=dict(Temperature=30, Humidity=60, PH=6.5, rain_fall=50, n=10, p=15, k=20))
        self.assertIn(b'Recommended Crop is', response.data)
if __name__ == '__main__':
    unittest.main()
