from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/stonks.html')
def login(request):
    return render(request, 'accounts/login.html')
def about(request):
    return render(request, 'accounts/about.html')
def contact(request):
    return render(request, 'accounts/contact.html')
def terms(request):
    return render(request, 'accounts/terms.html')
def signup(request):
    return render(request, 'accounts/signup.html')

# Create your views here.
