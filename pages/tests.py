from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class SimpleTestes(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
