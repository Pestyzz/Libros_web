from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard_app.models import Shopping, ShoppingItem, Book, Cart, CartItem

def payment_view(request):
    if request.method == "POST":
        client = request.user
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')

        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        
        total_paid = sum(item.book.price * item.quantity for item in cart_items)

        shopping = Shopping.objects.create(
            client=client,
            email=email,
            address=address,
            phone_number=phone_number,
            paid=total_paid,
            status='EP',
        )

        for item_data in cart_items:
            book = Book.objects.get(id = item_data.book.id)
            
            ShoppingItem.objects.create(
                shopping=shopping,
                product_id=book,
                quantity=item_data.quantity
            )

        cart_items.delete()

        messages.success(request, '¡Compra realizada con éxito!')

        # Redireccionar a la página de confirmación de compra o a donde sea necesario
        return redirect('home')  # Cambia esto por tu propia URL de confirmación

    # Si no es POST, podría ser GET u otro método, manejar según necesidades
    return render(request, 'payment.html')  # Asegúrate de que estás redirigiendo correctamente aquí
