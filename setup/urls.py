from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from evento.views import evento_home

urlpatterns = [path("admin/", admin.site.urls),
    path("", evento_home, name="home"),
    path("eventos/", include('evento.urls')),
    path("users/", include('users.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)