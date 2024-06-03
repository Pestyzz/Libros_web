from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboardHome'),
    path('charts/', views.dashboardCharts, name='dashboardCharts'),
    path('shopping/', views.dashboardShopping, name='dashboardShopping'),
    path('shopping_edit/', views.dashboardShoppingEdit, name='dashboardShoppingEdit'),
    path('orders/', views.dashboardOrders, name='dashboardOrders'),
    path('products/', views.dashboardProducts, name='dashboardProducts'),
    path('product_add/', views.dashboardProductAdd, name='dashboardProductAdd'),
    path('product_edit/', views.dashboardProductEdit, name='dashboardProductEdit'),
    path('users/', views.dashboardUsers, name='dashboardUsers'),
    path('user_add/', views.dashboardUserAdd, name='dashboardUserAdd')
]
