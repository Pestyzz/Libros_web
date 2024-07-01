from django.shortcuts import render, redirect
from django.contrib import messages
from dashboard_app.models import Shopping, ShoppingItem, Book

def payment_view(request):
    if request.method == "POST":
        client = request.user
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')

        cart = request.session.get('cart', {})

        total_paid = sum(item['totalPrice'] for item in cart.values())

        shopping = Shopping.objects.create(
            client=client,
            email=email,
            address=address,
            phone_number=phone_number,
            paid=total_paid,
            status='EP',
        )

        for item_id, item_data in cart.items():
            book = Book.objects.get(id = item_data['product_id'])
            
            ShoppingItem.objects.create(
                shopping=shopping,
                product_id=book,
                quantity=item_data['quantity']
            )

        request.session['cart'] = {}

        messages.success(request, '¡Compra realizada con éxito!')

        # Redireccionar a la página de confirmación de compra o a donde sea necesario
        return redirect('home')  # Cambia esto por tu propia URL de confirmación

    # Si no es POST, podría ser GET u otro método, manejar según necesidades
    return render(request, 'payment.html')  # Asegúrate de que estás redirigiendo correctamente aquí
