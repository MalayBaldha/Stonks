from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/stonks.html')
def contact(request):
    return HttpResponse('Contact page')

def customers(request):
    return HttpResponse('Customer page')
# Create your views here.
