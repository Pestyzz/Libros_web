from dashboard_app.lists import CATEGORIES
from dashboard_app.models import Cart, CartItem, Favorite, FavoriteItem

def cart_detail(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_cart = sum(item.book.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_cart = 0
    
    return {
        'cart_items': cart_items,
        'total_cart': total_cart,
    }
    
def favorite_detail(request):
    if request.user.is_authenticated:
        favorite, created = Favorite.objects.get_or_create(user=request.user)
        favorite_items = FavoriteItem.objects.filter(favorite=favorite)
    else:
        favorite_items = []
    
    return {'favorite_items': favorite_items}


def categories(request):
    return {"CATEGORIES": CATEGORIES}