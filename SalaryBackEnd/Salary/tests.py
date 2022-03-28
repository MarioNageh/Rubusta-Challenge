from django.test import TestCase
from django.test import Client
from Salary.models import Admins
from Salary.utils.authUtils import hashSha1


class AnimalTestCase(TestCase):
    def setUp(self):
        Admins.objects.create(firstName="Rubusta", lastName="Admin", email="Admin@Rubusta.com",
                              password=hashSha1("1234")
                              , phone="01208847854")

    def test_get_data_withoutLogin(self):
        c = Client()
        response = c.get('/salary/?month=12&year=2022')
        self.assertEqual(response.status_code, 401)
