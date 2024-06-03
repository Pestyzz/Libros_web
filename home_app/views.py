from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def product(request, id):
    return render(request, 'product.html')

def history(request):
    return render(request, 'history.html')