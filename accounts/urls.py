from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
]

