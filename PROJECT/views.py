from django.shortcuts import render,redirect

def home_page(request):
    return render( request,'home_page.html',)

def contact_page(request):
    return render( request,'contact.html',)

def profile_page(request):
    return render( request,'profile.html',)

def login_page(request):
    return render( request,'login.html',)

def authorize(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'abror' and password == '12345':
        return redirect("/")
    else:
        return redirect("/login")