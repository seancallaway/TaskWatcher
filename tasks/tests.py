from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import resolve
from tasks.models import Task
from tasks.views import HomePage

BOOTSTRAP_VERSION = 'bootstrap/4.4.1'


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, HomePage)

    def test_home_page_includes_bootstrap(self):
        response = self.client.get('/')
        self.assertContains(response, BOOTSTRAP_VERSION)


class TaskTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(name='Test Task')
        self.task.history.create(end_time=datetime(2020, 3, 19, 15, 7, 0), duration=timedelta(minutes=7))
        self.task.history.create(end_time=datetime(2020, 3, 19, 14, 6, 0), duration=timedelta(minutes=6))
        self.task.history.create(end_time=datetime(2020, 3, 19, 13, 5, 0), duration=timedelta(minutes=5))

    def test_avg_calculation(self):
        result = self.task.calc_avg_duration()
        self.assertEqual(result, timedelta(minutes=6))

    def test_saved_avg_calculation(self):
        self.assertEqual(self.task.avg_duration, timedelta(minutes=6))
