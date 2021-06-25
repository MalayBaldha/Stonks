from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/stonks.html')

def login(request):
    '''if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        client = Client.objects.get(Email = email)
        if Client.objects.get(Email = email,Password = password) == 1:
            return HttpResponseRedirect(reverse('accounts:client',args(email)))
        else:
            return render(request, 'accounts/login.html')
    else:'''
    client = Client.objects.get(id = 5)
    return render(request, 'accounts/login.html',{'client':client})        

def signup(request):
    return render(request, 'accounts/signup.html')

def about(request):
    return render(request, 'accounts/about.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def terms(request):
    return render(request, 'accounts/terms.html')

def client(request, ID):
    client = Client.objects.get(id = ID)
    stocks = client.client_stock_set.all()
    
    assets = 0
    for S in stocks:
        assets += (S.Shares*S.SID.Price)

    context = {'client': client, 'stocks': stocks, 'assets': assets}
    return render(request, 'accounts/client.html', context)

def broker(request, ID):
    broker = Broker.objects.get(id = ID)
    clients = broker.client_broker_set.all()
    cnt_cli = broker.client_broker_set.all().count()
    
    

    context = {'broker': broker, 'clients': clients, "cnt_cli": cnt_cli}
    return render(request, 'accounts/broker.html', context)


