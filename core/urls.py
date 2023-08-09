from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', include('contato.url')),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, documento_root= settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, documento_root= settings.STATIC_ROOT)