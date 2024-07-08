from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dashboard_app.lists import CATEGORIES
from dashboard_app.models import Book, Shopping, ShoppingItem, Cart, CartItem, Favorite, FavoriteItem

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

@login_required(login_url="/login/")
def cartAdd(request, product_id):
    product = get_object_or_404(Book, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    quantity = 1
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=product)
    if created:
        cart_item.quantity = quantity
    else:
         cart_item.quantity += quantity
         
    cart_item.save()
    return redirect("home")

@login_required(login_url="/login/")
def cartRemove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("home")

@login_required(login_url="/login/")
def favoriteAdd(request, product_id):
    product = get_object_or_404(Book, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user)
    favorite_item, created = FavoriteItem.objects.get_or_create(favorite=favorite, book=product)
         
    favorite_item.save()
    return redirect("home")

@login_required(login_url="/login/")
def favoriteRemove(request, item_id):
    favorite_item = get_object_or_404(FavoriteItem, id=item_id, favorite__user=request.user)
    
    favorite_item.delete()
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