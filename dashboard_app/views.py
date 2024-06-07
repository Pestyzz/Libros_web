from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .lists import BOOK_LANGUAGES, CATEGORIES
from .models import Book, CustomUser

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
    
    books = Book.objects.all()
    
    context = {
        "books": books
    }
    return render(request, 'products/products.html', context)

def dashboardProductAdd(request):
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'products/productadd.html', {
            "languages": BOOK_LANGUAGES,
            "categories": CATEGORIES
        })
    else:
        print("Obteniendo Datos")
        print(request.POST)
        
        try:
            isbn = request.POST["isbn"]
            book_name = request.POST["bookName"]
            author = request.POST["author"]
            publisher = request.POST["publisher"]
            language = request.POST["language"]
            description = request.POST["review"]
            image = request.FILES.get("bookImage")
            category = request.POST["category"]
            sub_category = request.POST["subCategory"]
            price = request.POST["price"].replace(".", "")
            price = int(price)
            
            publish = request.POST.get("publish") == "on"
            
            book = Book.objects.create(
                isbn=isbn,
                book_name=book_name,
                author=author,
                publisher=publisher,
                languages=language,
                description=description,
                image=image,
                category=category,
                sub_category=sub_category,
                price=price,
                publish=publish
            )
            
            book.save()
            return redirect('dashboardProducts')   
        except IntegrityError:
            return render(request, 'products/productadd.html', {
                "languages": BOOK_LANGUAGES,
                "categories": CATEGORIES,
                'error': "ISBN ya registrado."
            })
        
def dashboardProductEdit(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    
    context = {
        "book": book,
        "languages": BOOK_LANGUAGES,
        "categories": CATEGORIES
    }
    return render(request, 'products/productedit.html', context)

def dashboardProductDelete(request, isbn):
    
    return render(request, 'products/products.html')

def dashboardUsers(request):
    return render(request, 'users/users.html')

def dashboardUserAdd(request):
    return render(request, 'users/useradd.html')

def dashboardUserEdit(request):
    return render(request, 'users/useredit.html')