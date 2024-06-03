from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    context = {
        'register': True
    }
    return render(request, 'register.html', context)

def recover(request):
    return render(request, 'recover.html')
