from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, featured=True, inventory=100)
        expected_string = "IceCream : 80"
        actual_string = f"{item.title} : {item.price}"
        self.assertEqual(actual_string, expected_string)