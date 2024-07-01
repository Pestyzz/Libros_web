from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboardHome'),
    path('profile/', views.dashboardProfile, name='dashboardProfile'),
    path('charts/', views.dashboardCharts, name='dashboardCharts'),
    path('shopping/', views.dashboardShopping, name='dashboardShopping'),
    path('shopping_edit/<int:shopping_id>', views.dashboardShoppingEdit, name='dashboardShoppingEdit'),
    path('orders/', views.dashboardOrders, name='dashboardOrders'),
    path('products/', views.dashboardProducts, name='dashboardProducts'),
    path('product_add/', views.dashboardProductAdd, name='dashboardProductAdd'),
    path('product_edit/<int:isbn>', views.dashboardProductEdit, name='dashboardProductEdit'),
    path('product_delete/<int:isbn>', views.dashboardProductDelete, name='dashboardProductDelete'),
    path('users/', views.dashboardUsers, name='dashboardUsers'),
    path('user_add/', views.dashboardUserAdd, name='dashboardUserAdd'),
    path('user_edit/<int:id>', views.dashboardUserEdit, name='dashboardUserEdit')
]
