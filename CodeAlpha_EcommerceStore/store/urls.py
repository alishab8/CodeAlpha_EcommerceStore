from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("category/<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),

    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="store/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="product_list"), name="logout"),

    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:product_id>/", views.cart_remove, name="cart_remove"),

    path("order/create/", views.order_create, name="order_create"),
    path("orders/", views.order_history, name="order_history"),
]
