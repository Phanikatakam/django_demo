from django.shortcuts import render, redirect
from . models import samsungp,realmep,applep,epsonp
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'electronics/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'electronics/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def elec(request):
    return render(request,'electronics/home.html')

@login_required(login_url='login')
def electric(request):
    electronics = samsungp.objects
    return render(request, 'electronics/samsung.html', {'electronics': electronics})

@login_required(login_url='login')
def real(request):
    realme = realmep.objects
    return render(request, 'electronics/realme.html', {'realme': realme})

@login_required(login_url='login')
def apple(request):
    apples = applep.objects
    return render(request, 'electronics/apple.html', {'apples': apples})

@login_required(login_url='login')
def epson(request):
    epsons = epsonp.objects
    return render(request, 'electronics/epson.html', {'epsons': epsons})

@login_required(login_url='login')
def ellec(request):
    return render(request,'electronics/elect.html')

@login_required(login_url='login')
def about(request):
    return render(request,'electronics/about.html')

@login_required(login_url='login')
def payment(request):
    return render(request,'electronics/payment.html')

@login_required(login_url='login')
def contact(request):
    return render(request,'electronics/contact.html')
