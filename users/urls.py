from django.contrib import admin
from django.urls import path
from users.views import register_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'eventos'

urlpatterns = [path("admin/", admin.site.urls),
    path("register/", register_view, name="register")
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)