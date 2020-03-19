from datetime import datetime, timedelta
from time import sleep
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
        self.task.history.create(end_time=datetime(2020, 3, 19, 15, 0, 7), duration=timedelta(seconds=7))
        self.task.history.create(end_time=datetime(2020, 3, 19, 14, 0, 6), duration=timedelta(seconds=6))
        self.task.history.create(end_time=datetime(2020, 3, 19, 13, 0, 5), duration=timedelta(seconds=5))

    def test_avg_calculation(self):
        result = self.task.calc_avg_duration()
        self.assertEqual(result, timedelta(seconds=6))

    def test_saved_avg_calculation(self):
        self.assertEqual(self.task.avg_duration, timedelta(seconds=6))

    def test_toggle_creates_history(self):
        history_count = self.task.history.count()
        self.task.toggle()
        sleep(6)
        self.task.toggle()
        new_history_count = self.task.history.count()
        self.assertEqual(history_count + 1, new_history_count)

    def test_toggle_changes_running_state(self):
        task_running1 = self.task.is_running
        self.task.toggle()
        task_running2 = self.task.is_running
        self.task.toggle()
        self.assertFalse(task_running1)
        self.assertTrue(task_running2)
