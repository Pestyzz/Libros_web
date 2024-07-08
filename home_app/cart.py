from django.contrib import messages
from dashboard_app.models import Cart as CartModel

class Cart:
    def __init__(self, request):
        self.request = request
        self.user = request.user
        if self.user.is_authenticated:
            try:
                cart_instance, created = CartModel.objects.get_or_create(user=self.user)
                self.cart = cart_instance.data
            except CartModel.DoesNotExist:
                self.cart = {}
        else:
            self.session = request.session
            cart = self.session.get("cart")
            if not cart:
                self.session["cart"] = {}
                self.cart = self.session["cart"]
            else:
                self.cart = cart
    
    def add(self, product):
        id = str(product.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "product_id": product.id,
                "image": product.image.url,
                "name": product.book_name,
                "price": product.price,
                "totalPrice": product.price,
                "quantity": 1,
            }
            messages.success(self.request, f'El libro "{product.book_name}" ha sido añadido al carro.')
        else:
            self.cart[id]["quantity"] += 1
            self.cart[id]["totalPrice"] += product.price
            messages.info(self.request, f'Se ha añadido otra unidad del libro "{product.book_name}" al carro.')
        self.save()
        
    def remove(self, product):
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]["quantity"] -= 1
            self.cart[id]["totalPrice"] -= product.price
            if self.cart[id]["quantity"] <= 0: 
                self.delete(product)
            else:
                messages.info(self.request, f'Una unidad del libro "{product.book_name}" ha sido removida del carro.')
            self.save()

    def delete(self, product):
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            messages.warning(self.request, f'El libro "{product.book_name}" ha sido removido del carro.')
            self.save()

    def save(self):
        if self.user.is_authenticated:
            CartModel.objects.update_or_create(user=self.user, defaults={'data': self.cart})
        else:
            self.session["cart"] = self.cart
            self.session.modified = True
    
    def clean(self):
        self.cart = {}
        if self.user.is_authenticated:
            CartModel.objects.filter(user=self.user).update(data=self.cart)
        else:
            self.session["cart"] = {}
            self.session.modified = True
