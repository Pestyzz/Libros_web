from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('login/', include('login_app.urls')),
    path('payment/', include('payment_app.urls')),
    path('dashboard/', include('dashboard_app.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
