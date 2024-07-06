from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from dashboard_app.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

def signin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
           
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return render(request, 'login.html', {
                "error": "El Usuario/Contraseña son incorrectos"
            })
        else:
            login(request, user)
            return redirect('home')
                        
def signout(request):
    logout(request)
    return redirect("home")

def register(request):    
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'register.html', {
            'register': True
        })
    else:
        print("Obteniendo datos")
        print(request.POST)
        
        try:
            username = request.POST["username"]
            first_name = request.POST["firstName"]
            lastNames = request.POST["lastNames"].split()
            surname = lastNames[0]
            last_name = lastNames[1]
            email = request.POST["email"]
            phone = request.POST["phone"]
            password = request.POST["password"] 
            address = request.POST["address"]
                
            user = CustomUser.objects.create(
                username = username,
                password = make_password(password),
                email = email,
                phone_number = phone,
                first_name = first_name,
                surname = surname,
                last_name = last_name,
                address = address
            )

            user.save()
            return redirect("login")            
        except IntegrityError:
            return render(request, 'register.html', {
                'register': True,
                'error': "Usuario o Email ya existen."
            })

def recover(request):
    return render(request, 'recover.html')
