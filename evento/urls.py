from django.contrib import admin
from django.urls import path
from evento.views import EventoCreateView, EventoListView, evento_page, EventoDeleteView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'evento'

urlpatterns = [path("admin/", admin.site.urls),
    path("", EventoListView.as_view(), name="evento_list"),
    path("create", EventoCreateView.as_view(), name="evento_create"),
    path('evento/delete/<slug:slug>/', EventoDeleteView.as_view(), name='evento_delete'),
    path("<slug:slug>", evento_page, name="evento_page")
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)