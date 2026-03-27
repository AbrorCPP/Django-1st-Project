from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from app_data.models import Product 
from django.contrib.auth.models import User


def home_page(request):
    product = Product.objects.all().order_by("name")

    data = {
        "product" : product
    }
    return render( request,'home_page.html',context = data)

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

def register_page(request):
    return render( request,'registration.html',)

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

def register_user(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')


    #Guard-clause
    if password1 != password2:
        return redirect("register")
    
    user_exists = User.objects.filter(username = username).exists()

    if user_exists:
        return redirect("register")
    
    new_user = User.objects.create(
        first_name = first_name,
        last_name = last_name,
        username = username,
        email = email,
    )

    new_user.set_password(raw_password=password2)

    new_user.save()

    return redirect("login")


    

    


