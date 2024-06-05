from django.urls import path
from . import views
from login_app.views import signout

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', signout, name='logout'),
    path('product/<int:id>', views.product, name='product'),
    path('history/', views.history, name='myhistory')
]
