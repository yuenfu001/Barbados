from django.test import TestCase
from django.urls import reverse
from .models import DriverInfo
from .forms import DriverCreate

# Create your tests here.

class DriverViewTest(TestCase):
    def test_add_driver(self):
        response = self.client.post(reverse('drivers:add_driver'), {
            'first_name': 'John',
            'last_name': 'Doe',
            # Add other required form fields
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission

        # Check if the driver was added to the database
        self.assertTrue(DriverInfo.objects.filter(first_name='John', last_name='Doe').exists())

    # Add more tests for other functionalities
