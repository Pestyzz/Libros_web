from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='login'),
    path('register/', views.register, name='register'),
    path('recover_account/', views.recover, name='recover')
]
