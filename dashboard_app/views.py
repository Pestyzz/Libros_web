from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboardProfile(request):
    return render(request, 'adminprofile.html')

def dashboardCharts(request):
    return render(request, 'charts.html')

def dashboardShopping(request):
    return render(request, 'shopping/shopping.html')

def dashboardShoppingEdit(request):
    return render(request, 'shopping/shoppingedit.html')

def dashboardOrders(request):
    return render(request, 'orders.html')

def dashboardProducts(request):
    return render(request, 'products/products.html')

def dashboardProductAdd(request):
    return render(request, 'products/productadd.html')

def dashboardProductEdit(request):
    return render(request, 'products/productedit.html')

def dashboardUsers(request):
    return render(request, 'users/users.html')

def dashboardUserAdd(request):
    return render(request, 'users/useradd.html')

def dashboardUserEdit(request):
    return render(request, 'users/useredit.html')