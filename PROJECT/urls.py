from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def home_page(request):
    return render(
        request,
        'home_page.html',
    )

def contact_page(request):
    return render(
        request,
        'contact.html',
    )

def profile_page(request):
    return render(
        request,
        'profile.html',
    )
urlpatterns = [
    path(route="", view=home_page),
    path(route="contact", view=contact_page),
    path(route="profile", view=profile_page),
]
