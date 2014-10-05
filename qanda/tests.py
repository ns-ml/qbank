from django.test import TestCase
from django.core.urlresolvers import resolve
from qanda.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		address = resolve('/')
		self.assertEqual(address.func, home_page)