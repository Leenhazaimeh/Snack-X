from django.test import TestCase

# Create your tests here.
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='snack@gmail.com',
            password='1234'
        )
        self.snack = Snack.objects.create(
            title='potato',
            purshaser=self.user,
            description='potato and ketchup'
        )

    

    def test_num_one(self):
        self.assertEqual(str(self.snack), "potato")

    

    def test_num_two(self):
        self.assertEqual(self.snack.title, 'potato')
        self.assertEqual(str(self.snack.purshaser), 'snack@gmail.com')
        self.assertEqual(self.snack.description, 'potato and ketchup')

   
    def test_snack_num_three(self):
        expected = 200
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, expected)
        self.assertContains(response, "potato")
        self.assertTemplateUsed(response, "snacks/snack_list.html")

    

