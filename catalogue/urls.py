from django.urls import path
from catalogue.views import index, home, contacts

urlpatterns = [
    path('index/', index),
    path('home/', home),
    path('contacts/', contacts)
]
