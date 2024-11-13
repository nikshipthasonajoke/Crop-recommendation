import unittest
from app import app

class FlaskTest(unittest.TestCase):

    # Ensure that the welcome page returns a 200 status code
    def test_welcome_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Ensure that the predict route returns a 200 status code
    def test_predict_route(self):
        tester = app.test_client(self)
        response = tester.post('/predict', data=dict(Temperature=30, Humidity=60, PH=6.5, rain_fall=50, n=10, p=15, k=20))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Ensure that the prediction form contains necessary elements
    def test_prediction_form_elements(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Temperature:', response.data)
        self.assertIn(b'Humidity:', response.data)
        self.assertIn(b'PH in the soil:', response.data)
        self.assertIn(b'Rain Fall:', response.data)
        self.assertIn(b'Potassium (K) in the Soil:', response.data)
        self.assertIn(b'Nitrogen (N) in the Soil:', response.data)
        self.assertIn(b'Phosphorous (P) in the Soil:', response.data)
        self.assertIn(b'Predict', response.data)

    # Ensure that the prediction form is submitted correctly
    def test_prediction_form_submission(self):
        tester = app.test_client(self)
        response = tester.post('/predict', data=dict(Temperature=30, Humidity=60, PH=6.5, rain_fall=50, n=10, p=15, k=20))
        self.assertIn(b'Recomended Crop is MOTH BEANS', response.data)

if __name__ == '__main__':
    unittest.main()
