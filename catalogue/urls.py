from django.urls import path
from catalogue.views import index, home, contacts

urlpatterns = [
    path('', index),
    path('', home),
    path('', contacts)
]
