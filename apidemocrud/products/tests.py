from django.test import TestCase
from faker import Faker
from model_mommy import mommy
from ninja.testing import TestClient

from apidemocrud.products.api import router_api
from apidemocrud.products.models import Client

client = TestClient(router_api)
fake = Faker()


class TestesDemoCrud(TestCase):
    def setUp(self):
        self.client_user = mommy.make(Client,
                                      name=fake.name,
                                      key=fake.uuid4())

    def test_auth(self):
        response = client.get(f"/auth?api_key={self.client_user.key}")
        self.assertEqual(response.json(), f"Authenticated {self.client_user.name}")
        self.assertEqual(response.status_code, 200)

    def test_auth_unauthorized(self):
        response = client.get(f"/auth?api_key={fake.uuid4()}")
        unauthorized = {
            'detail': 'Unauthorized'
        }
        self.assertEqual(response.json(), unauthorized)
        self.assertEqual(response.status_code, 401)
