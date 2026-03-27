from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path(route="", view=views.home_page,name = "home_page"),
    path(route="contact/", view=views.contact_page, name = "contact"),
    path(route="profile/", view=views.profile_page,name = "profile"),
    path(route="login/", view=views.login_page, name = "login"),
    path(route="authorize/", view=views.authorize, name = "authorize"),
    path(route="logout/", view=views.user_logout, name = "logout"),
    path(route="signup/", view=views.register_page,name = "register"),
    path(route="signup_t", view = views.register_user,name = "register_post")
]
