from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from miapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('miapp/', include('miapp.urls')),  # Incluye las urls de tu aplicación miapp
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
