from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')

def product(request, id):
    return render(request, 'product.html')

@login_required
def history(request):
    return render(request, 'history.html')