from django.shortcuts import render, redirect
from .import forms
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')

def contactUs(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success!')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong, try again later or please send me an email: web\'still@gmail.com')
    context = {'form': form}
    return render(request, 'contact.html', context)

def Impressions(request):
    return render(request, 'impressions.html')

def pricing(request):
    return render(request, 'pricing.html')

def reference(request):
    return render(request, 'reference.html')

def responsive(request):
    return render(request, 'responsive.html')

def services(request):
    return render(request, 'services.html')

def collega(request):
    return render(request, 'team-member.html')

def WebDev(request):
    return render(request, 'webdeveloping.html')

def Process(request):
    context = {}
    return render(request, 'work-process.html', context)

def success(request):
    return render(request, 'successfully.html')

def offerRequest(request):
    form = forms.Basic()
    
    if request.method == 'POST':
        form = forms.Basic(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The offer request was successful!')
            return redirect('success')
        else:
            messages.error(request, 'The offer request was not successful!')
    
    context = {'form': form}
    return render(request, 'offer-request.html', context)