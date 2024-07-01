from django.contrib import messages

class Favorite:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        favorite = self.session.get("favorite")
        if not favorite:
            self.session["favorite"] = {}
            self.favorite = self.session["favorite"]
        else:
            self.favorite = favorite
    
    def add(self, product):
        id = str(product.id)
        if id not in self.favorite.keys():
            self.favorite[id] = {
                "product_id": product.id,
                "image": product.image.url,
                "name": product.book_name,
                "price": product.price,
                "quantity": 1
            }
            
            messages.success(self.request, f'El libro "{product.book_name}" ha sido añadido a favoritos.')
        else:
            messages.info(self.request, f'El libro "{product.book_name}" ya está en sus favoritos.')
        self.save()
            
    def remove(self, product):
        id = str(product.id)
        if id in self.favorite.keys():
            self.favorite[id]["quantity"] -= 1
            if self.favorite[id]["quantity"] <= 0: self.delete(product)
            self.save()

    def delete(self, product):
        id = str(product.id)
        if id in self.favorite:
            del self.favorite[id]
            messages.warning(self.request, f'El libro "{product.book_name}" ha sido eliminado de favoritos.')
            self.save()

    def save(self):
        self.session["favorite"] = self.favorite
        self.session.modified = True
    
    def clean(self):
        self.session["favorite"] = {}
        self.session.modified = True