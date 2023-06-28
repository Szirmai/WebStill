from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from  .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import logout as auth_logout
from .import models
from main.models import Contact as contacts
from main.models import Offer as offers

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Renamed to auth_login
            messages.success(request, 'If you were a hacker, congratulations. You are in!')
            return redirect('dash-home')
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')
    else:
        return HttpResponse('Sztem próbáld újra néha szarakszik a rendszer')
    context = {}
    return render(request, 'dash/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

# Create your views here.
@login_required(login_url='login')
def home(request):
    learn = models.Learn.objects.all()
    contact = contacts.objects.all().order_by('-created')
    offer = offers.objects.all()
    
    context = {'learn': learn, 'contact': contact, 'offers': offer}
    return render(request, 'dash/index.html', context)

@login_required(login_url='login')
def offerRequest(request, pk):
    offer = offers.objects.get(created=pk)
    
    context = {'offers': offer}
    return render(request, 'dash/offer.html', context)

@login_required(login_url='login')
def offerRequests(request):
    offer = offers.objects.all()
    
    context = {'offers': offer}
    return render(request, 'dash/offers.html', context)

@login_required(login_url='login')
def Contact(request, pk):
    contact = contacts.objects.get(id=pk)
    
    context = {'contacts': contact}
    return render(request, 'dash/message.html', context)

@login_required(login_url='login')
def Contacts(request):
    contact = contacts.objects.all()
    
    context = {'contact': contact}
    return render(request, 'dash/messages.html', context)

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Renamed to auth_login
            messages.success(request, 'If you were a hacker, congratulations. You are in!')
            return redirect('dash-home')
        else:
            messages.info(request, 'Helytelen felhasználónév vagy jelszó')
            
    context = {}
    return render(request, 'dash/login.html', context)

def logout_view(request):
    auth_logout(request)
    return redirect('login')