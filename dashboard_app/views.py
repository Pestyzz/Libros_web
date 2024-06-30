from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
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

    return render(request, 'products/products.html', {"books": books})

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
                'error': "ISBN ya existente."
            })
        
def dashboardProductEdit(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    
    context = {
        "book": book,
        "languages": BOOK_LANGUAGES,
        "categories": CATEGORIES
    }
    
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'products/productedit.html', context)
    else:
        print("Obteniendo datos")
        print(request.POST)
        
        book_name = request.POST.get("bookName")
        author = request.POST.get("author")
        publisher = request.POST.get("publisher")
        language = request.POST.get("language")
        description = request.POST.get("review")
        image = request.FILES.get("bookImage")
        category = request.POST.get("category")
        sub_category = request.POST.get("subCategory")
        price = request.POST.get("price").replace(".", "")
        price = int(price)
        publish = request.POST.get("publish") == "on"       
        
        book.book_name = book_name
        book.author = author
        book.publisher = publisher
        book.languages = language
        book.description = description
        if image:
            book.image = image
        book.category = category
        book.sub_category = sub_category
        book.price = price
        book.publish = publish

        book.save()
        
        return redirect("dashboardProducts")

def dashboardProductDelete(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    
    if request.method == "POST":
        book.delete()
        return redirect("dashboardProducts")
    
    return redirect("dashboardProducts")

def dashboardUsers(request):
    users = CustomUser.objects.all
    
    return render(request, 'users/users.html', {"users": users})

def dashboardUserAdd(request):
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'users/useradd.html')
    else:
        print("Obteniendo Datos")
        print(request.POST)
        
        try:
            username = request.POST.get("user")
            first_name = request.POST.get("name")
            lastNames = request.POST.get("lastnames").split()
            surname = lastNames[0]
            last_name = lastNames[1]
            email = request.POST.get("email")
            password = request.POST.get("psw")
            phone_number = request.POST.get("phone")
            
            if request.POST.get("typeuser") == "2":
                is_superuser = True
                is_staff = True
            else:
                is_superuser = False
                is_staff = False
            
            address = request.POST.get("address")
            
            user = CustomUser.objects.create(
                username = username,
                password = make_password(password),
                email = email,
                first_name = first_name,
                surname = surname,
                last_name = last_name,
                phone_number = phone_number,
                address = address,
                is_superuser = is_superuser,
                is_staff = is_staff
            )
            
            user.save()
            return redirect('dashboardUsers')   
        except IntegrityError as e:
            return render(request, 'users/users.html', {
                'error': "Usuario o Email ya existen."
            })

def dashboardUserEdit(request, id):
    user = get_object_or_404(CustomUser, id=id)
    
    if request.method == "GET":
        print("Enviando datos")
        return render(request, 'users/useredit.html', {"user": user})
    else:
        print("Obteniendo datos")
        print(request.POST)
        
        try:
            username = request.POST.get("user")
            first_name = request.POST.get("name")
            lastNames = request.POST.get("lastnames").split()
            surname = lastNames[0]
            last_name = lastNames[1]
            email = request.POST.get("email")
            password = request.POST.get("psw")
            phone_number = request.POST.get("phone")
            
            user_type = request.POST.get("userType")
            if user_type == "True":
                is_superuser = True
                is_staff = True
            else:
                is_superuser = False
                is_staff = False
            
            address = request.POST.get("address")
            
            user.username = username
            if password:
                user.password = make_password(password)
            user.email = email
            user.first_name = first_name
            user.surname = surname
            user.last_name = last_name
            user.phone_number = phone_number
            user.address = address
            user.is_superuser = is_superuser
            user.is_staff = is_staff

            user.save()
            
            return redirect("dashboardUsers")
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            return render(request, 'users/useredit.html', {
                'user': user,
                'error': "Usuario o Email ya existen."
            })
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'users/useredit.html', {
                'user': user,
                'error': "Ocurrió un error inesperado. Por favor, intente de nuevo."
            })
        