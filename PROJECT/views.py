from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

def home_page(request):
    return render( request,'home_page.html',)

def contact_page(request):
    return render( request,'contact.html',)

def profile_page(request):
    if request.user.is_authenticated:
        return render( request,'profile.html',)
    else:
        return redirect('/login/')

def login_page(request):
    if not request.user.is_authenticated:
        return render( request,'login.html',)
    else:
        return redirect('/')

def authorize(request):
    username = request.POST['username']
    password = request.POST['password']

    # Bazadan barcha foydalanuvchilarni olib chiqish
    # Ular orasidan frontendan kelgan ma'lumotlarga mos tushadigan qiymat qaytarish
    # Agar topilsa - tizimga kirish
    # Agar topilmasa unda kirish sahifasida qolish

    #ORM object ralational mapping
    # users = User.objects.all()
    # # select * all from user
    # user = users.filter(username=username).first() # []
    #
    # if user is None:
    #     return redirect('/login')
    # else:
    #     if user.check_password(password):
    #         #Brauzerda shu foydalanuvchi va shu so'rov uchun sessio id hosil qilish
    #         login(request,user)
    #         return redirect('/')
    #     else:
    #         return redirect("/login/")
    user = authenticate(
        username=username,
        password=password,
    )

    if user:
        login(request, user)
        return redirect("/")
    else:
        return redirect("/login/")

def user_logout(request):
    logout(request)
    return redirect("/login/")


