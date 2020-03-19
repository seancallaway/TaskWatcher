from django.test import TestCase
from django.urls import resolve
from tasks.views import HomePage

BOOTSTRAP_VERSION = 'bootstrap/4.4.1'


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, HomePage)

    def test_home_page_includes_bootstrap(self):
        response = self.client.get('/')
        self.assertContains(response, BOOTSTRAP_VERSION)
