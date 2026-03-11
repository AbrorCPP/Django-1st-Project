from django.shortcuts import render

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

def login_page(request):
    return render(
        request,
        'login.html',
    )