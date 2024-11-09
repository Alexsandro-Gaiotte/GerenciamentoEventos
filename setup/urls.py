from django.contrib import admin
from django.urls import path, include
from evento.views import EventoCreateView, EventoListView, evento_page
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [path("admin/", admin.site.urls),
    path("", include('evento.urls')),
    path("users/", include('users.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)