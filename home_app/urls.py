from django.urls import path
from . import views
from login_app.views import signout, login

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product, name='product'),
    path('catalogue/', views.finder, name='finder'),
    path('catalogue/<str:category>', views.finder, name='finderCategory'),
    path('add/<int:product_id>', views.cartAdd, name='add'),
    path('remove/<int:product_id>', views.cartRemove, name='remove'),
    path('delete/<int:product_id>', views.cartDelete, name='delete'),
    path('cls/', views.cartClean, name='cls'),
    path('fav_add/<int:product_id>', views.favAdd, name='favAdd'),
    path('fav_remove/<int:product_id>', views.favRemove, name='favRemove'),
    path('fav_delete/<int:product_id>', views.favDelete, name='favDelete'),
    path('fav_cls/', views.favClean, name='favCls'),
    path('logout/', signout, name='logout'),
    path('history/', views.history, name='history')
]
