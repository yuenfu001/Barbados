from django.test import TestCase
from django.urls import reverse
from .models import TruckInfo
from .forms import TruckCreate

# Create your tests here.

class TruckViewTest(TestCase):
    def test_add_truck(self):
        response = self.client.post(reverse('trucks:add_truck'), {
            'bl_number': '12345',
            'plate_number': 'ABC123',
            # Add other required form fields
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission

        # Check if the truck was added to the database
        self.assertTrue(TruckInfo.objects.filter(bl_number='12345', plate_number='ABC123').exists())

    # Add more tests for other functionalities
