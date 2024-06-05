from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from dashboard_app.models import CustomUser

# Create your views here.

def login(request):
    
    return render(request, 'login.html')

def register(request):
    context = {
        'register': True
    }
    
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'register.html', context)
    else:
        print("Obteniendo datos")
        print(request.POST)
        username = request.POST["username"]
        first_name = request.POST["firstName"]
        
        lastNames = request.POST["lastNames"].split()
        surname = lastNames[0]
        last_name = lastNames[1]
        
        email = request.POST["email"]
        phone = request.POST["phone"]

        password = request.POST["password"]
        
        address = request.POST["address"]
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return redirect("register")
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Ya existe una cuenta con ese correo.")
            return redirect("register")
        
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
        messages.success(request, "Su cuenta se ha creado correctamente.")
        
        return redirect("login")
        

def recover(request):
    return render(request, 'recover.html')
