from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dashboard_app.lists import CATEGORIES
from dashboard_app.models import Book, Shopping, ShoppingItem
from home_app.cart import Cart
from home_app.favorite import Favorite

# Create your views here.

def home(request):
    books = Book.objects.all()
    
    return render(request, 'index.html', {"books": books})

def product(request, id):
    books = get_object_or_404(Book, id = id)
    return render(request, 'product.html', {"book": books})

def finder(request, category=None):
    books = None

    if request.method == "GET":
        searchQuery = request.GET.get("search", "")

        category_filters = {cat[1]: cat[0] for cat in CATEGORIES}

        if category in category_filters:
            filter_criteria = category_filters[category]
            books = Book.objects.filter(Q(category=filter_criteria) & Q(book_name__icontains=searchQuery))
        else:
            books = Book.objects.filter(Q(book_name__icontains=searchQuery) | Q(publisher__icontains=searchQuery))

        data = {
            "searchQ": searchQuery,
            "books": books,
            "category": category
        }

        return render(request, "finder.html", data)


def cartAdd(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id = product_id)
    cart.add(product)
    return redirect("home")

def cartRemove(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id = product_id)
    cart.remove(product)
    return redirect("home")

def cartDelete(request, product_id):
    cart = Cart(request)
    product = Book.objects.get(id = product_id)
    cart.delete(product)
    return redirect("home")

def cartClean(request):
    cart = Cart(request)
    cart.clean()
    return redirect("home")

def favAdd(request, product_id):
    if request.user.is_authenticated:
        favorite = Favorite(request)
        product = Book.objects.get(id = product_id)
        favorite.add(product)
        return redirect("home")
    else:
        return redirect("login")

def favRemove(request, product_id):
    favorite = Favorite(request)
    product = Book.objects.get(id = product_id)
    favorite.remove(product)
    return redirect("home")

def favDelete(request, product_id):
    favorite = Favorite(request)
    product = Book.objects.get(id = product_id)
    favorite.delete(product)
    return redirect("home")

def favClean(request):
    favorite = Favorite(request)
    favorite.clean()
    return redirect("home")

@login_required(login_url="/login/")
def history(request):
    if request.user.is_authenticated:
        user = request.user
        purchases = Shopping.objects.filter(client=user)
        items = ShoppingItem.objects.filter(shopping__in=purchases)
        
        return render(request, 'history.html', {"purchases": purchases, "items": items})
    else:
        return redirect("login")