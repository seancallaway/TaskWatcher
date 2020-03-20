from django.views.generic import ListView
from tasks.models import Task


class HomePage(ListView):
    template_name = 'index.html'
    model = Task
    queryset = Task.objects.all().order_by('last_start')
    context_object_name = 'tasks'
