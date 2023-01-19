from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import User

class BankTests(APITestCase):
    def test_post_unauthenticated_bank(self):
        data = {'bank_name': 'Suramericano'}
        response = self.client.post('/api/bank', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_bank(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'bank_name': 'Suramericano'}
        response = self.client.post('/api/bank', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
     
    def test_get_bank(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'bank_name': 'Suramericano'}
        self.client.post('/api/bank', data, format='json')
        
        data1 = {'bank_name': 'Hispanoamericano'}
        self.client.post('/api/bank', data1, format='json')
        
        response = self.client.get('/api/bank', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

      
    def test_get_a_bank(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'bank_name': 'Suramericano'}
        response = self.client.post('/api/bank', data, format='json')
        response_json = response.json()

        response = self.client.get(f'/api/bank-CRUD/{response_json["id"]}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_update_bank(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {'bank_name': 'Suramericano'}
        response = self.client.post('/api/bank', data, format='json')
        response_json = response.json()
        
        data_update = {'bank_name': 'Centroamericano'}
        response = self.client.put(f'/api/bank-CRUD/{response_json["id"]}', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       

    def test_delete_bank(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {'bank_name': 'Suramericano'}
        response = self.client.post('/api/bank', data, format='json')
        response_json = response.json()
        
        response = self.client.delete(f'/api/bank-CRUD/{response_json["id"]}', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
class ProviderTests(APITestCase):
    def test_post_unauthenticated_provider(self):
        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        response = self.client.post('/api/provider', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
        
    def test_create_provider(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 

        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        response = self.client.post('/api/provider', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_get_provider(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
             
        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        self.client.post('/api/provider', data, format='json')
        
        response = self.client.get('/api/provider', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

     
    def test_get_a_provider(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        response = self.client.post('/api/provider', data, format='json')
        response_json = response.json()

        response = self.client.get(f'/api/provider-CRUD/{response_json["id"]}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_update_provider(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        response = self.client.post('/api/provider', data, format='json')
        response_json = response.json()
        
        data_update = {
                "provider_name": "Marcela Steel S.A.",
                "nit_provider": "902566641-3",
                "contact_name": "Brayan Mendoza",
                "cell_phone_contact": "3004301911"
        }
        response = self.client.put(f'/api/provider-CRUD/{response_json["id"]}', data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_provider(self):
        user = User.objects.create_user('test@test.com', 'testsecret')
        self.client = APIClient()
        self.client.force_authenticate(user=user) 
        
        data = {
                "provider_name": "Laura Buenaventura S.A.S.",
                "nit_provider": "901866782-2",
                "contact_name": "Rodolfo Castro",
                "cell_phone_contact": "3006503944"
        }
        response = self.client.post('/api/provider', data, format='json')
        response_json = response.json()
        
        response = self.client.delete(f'/api/provider-CRUD/{response_json["id"]}', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
