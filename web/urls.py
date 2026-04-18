from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
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
    path(route="signup_t", view = views.register_user,name = "register_post"),
    path(route="add_product/", view = views.add_product,name = "add_product"),
    path(route='delete-product/<int:product_id>',view = views.delete_product, name = "delete_product"),
    path(route='product-details/<int:product_id>',view = views.product_detail, name = "product_detail"),
    path(route='edit-product/<int:product_id>',view = views.edit_product, name = "edit_product"),
]

urlpatterns += static(prefix = settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)