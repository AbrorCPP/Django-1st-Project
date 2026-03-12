from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path(route="", view=views.home_page),
    path(route="contact/", view=views.contact_page),
    path(route="profile/", view=views.profile_page),
    path(route="login/", view=views.login_page),
    path(route="authorize/", view=views.authorize),
]
