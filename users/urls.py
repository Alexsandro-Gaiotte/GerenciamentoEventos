from django.contrib import admin
from django.urls import path
from users.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),    
    path("logout/", logout_view, name="logout")    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)