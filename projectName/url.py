from django.urls import path
from projectName.views import hello_geeks

urlpatterns = [
    path('geek/', hello_geeks),
]