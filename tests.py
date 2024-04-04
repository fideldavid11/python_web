from django.test import TestCase
from django.urls import reverse

class MyappTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "¡Hola, mundo!")
