from django.urls import path
from tasks.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
