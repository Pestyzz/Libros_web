from django.urls import path
from . import views
from login_app.views import signout, login

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product, name='product'),
    path('catalogue/', views.finder, name='finder'),
    path('catalogue/<str:category>', views.finder, name='finderCategory'),
    path('add/<int:product_id>', views.cartAdd, name='add'),
    path('remove/<int:item_id>', views.cartRemove, name='remove'),
    path('fav_add/<int:product_id>', views.favoriteAdd, name='favAdd'),
    path('fav_remove/<int:item_id>', views.favoriteRemove, name='favRemove'),
    path('logout/', signout, name='logout'),
    path('history/', views.history, name='history')
]
