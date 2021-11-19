from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.

class TestAPI(TestCase):

    # Test endpoints Autenticación

    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/rest-auth/registration/', 
            {
                "username": "test_signUp",
                "password1": "test_signUp2021",
                "password2": "test_signUp2021",
                "email": "test_signUp@hydroverse.com"
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_login(self):
        client = APIClient()
        response = client.post(
            '/rest-auth/login/', 
            {
                "username": "hydroverse",
                "password": "9*/hydroverse/*23"
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('key' in  response.data.keys(), True)


    # Test endpoints Device State
    
    def test_get_devicestate(self):
        client = APIClient()
        response = client.get('/device/registration/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_devicestate(self):
        client = APIClient()
        response = client.get('/device/registration/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('name' in  response.data.keys(), True)
        self.assertEqual('description' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)      
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('active' in  response.data.keys(), True)
        self.assertEqual('users' in  response.data.keys(), True)


    def test_create_devicestate(self):
        client = APIClient()
        response = client.post(
            '/device/registration/', 
            {
                "name": "PRUEBA-8266",
                "description": "esto es una prueba",
                "pump_state": False,
                "comp_state": False,
                "light_state": False,
                "active": True,
                "users": [
                    1
                ]
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('name' in  response.data.keys(), True)
        self.assertEqual('description' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)      
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('active' in  response.data.keys(), True)
        self.assertEqual('users' in  response.data.keys(), True)


    def test_update_devicestate(self):
        client = APIClient()
        response = client.put(
            '/device/registration/1/',
            {
                "name": "PRUEBA-8266",
                "description": "esto es una prueba",
                "pump_state": False,
                "comp_state": False,
                "light_state": False,
                "active": True,
                "users": [
                    1
                ]
            },  
            format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('name' in  response.data.keys(), True)
        self.assertEqual('description' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)      
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('active' in  response.data.keys(), True)
        self.assertEqual('users' in  response.data.keys(), True)


    def test_delete_devicestate(self):
        client = APIClient()
        response = client.delete('/device/registration/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # Test endpoints Device History

    def test_get_devicehistory(self):
        client = APIClient()
        response = client.get('/device/history/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_devicehistory(self):
        client = APIClient()
        response = client.get('/device/history/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('date' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('device_id' in  response.data.keys(), True)


    def test_create_devicehistory(self):
        client = APIClient()
        response = client.post(
            '/device/history/', 
            {
                "pump_state": True,
                "comp_state": False,
                "light_state": False,
                "device_id": 1
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('date' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('device_id' in  response.data.keys(), True)


    def test_update_devicehistory(self):
        client = APIClient()
        response = client.put(
            '/device/history/1/',
            {
                "pump_state": True,
                "comp_state": False,
                "light_state": True,
                "device_id": 1
            }, 
            format='json') 

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('id' in  response.data.keys(), True)
        self.assertEqual('date' in  response.data.keys(), True)
        self.assertEqual('pump_state' in  response.data.keys(), True)
        self.assertEqual('comp_state' in  response.data.keys(), True)
        self.assertEqual('light_state' in  response.data.keys(), True)
        self.assertEqual('device_id' in  response.data.keys(), True)



    def test_delete_devicehistory(self):
        client = APIClient()
        response = client.delete('/device/history/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)