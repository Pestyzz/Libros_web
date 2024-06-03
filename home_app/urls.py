from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>', views.product, name='product'),
    path('history/', views.history, name='myhistory')
]
