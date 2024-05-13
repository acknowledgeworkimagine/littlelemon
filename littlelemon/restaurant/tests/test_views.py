from django.test import TestCase, override_settings
from django.urls import reverse
from restaurant.models import MenuItem  # Import your MenuItem model


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        MenuItem.objects.create(title="Menu 1", price=10.99, featured=True, inventory=10)
        MenuItem.objects.create(title="Menu 2", price=15.99, featured=True, inventory=20)
        MenuItem.objects.create(title="Menu 3", price=12.50, featured=True, inventory=30)

    def test_getall(self):
        # Retrieve all MenuItem objects
        response = self.client.get(reverse('menu-list'))  # Is the URL name for the view
        self.assertEqual(response.status_code, 200)

        # Serialize the retrieved objects
        serialized_data = response.data  # Assuming the response data is already serialized
        
        # Add your assertions to check if the serialized data equals the response
        self.assertEqual(len(serialized_data), 3)  # Assuming we added 3 Menu instances in the setup
        # Add more assertions as needed to check the serialized data