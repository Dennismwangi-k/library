from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_request, name="register"),
    path('contact-us/', views.contact, name="contact"),
    path("login", views.login_request, name="login"),
    path("home-after-login", views.home_after_login, name="home-after-login"),
    path("profile", views.profile, name="profile"),
]
    
