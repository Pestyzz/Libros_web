from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('login/', include('login_app.urls')),
    path('dashboard/', include('dashboard_app.urls'))
]
