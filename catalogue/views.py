from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "catalogue/index.html")


def home(request):
    return render(request, "catalogue/home.html")


def contacts(request):
    return render(request, "catalogue/contacts.html")
