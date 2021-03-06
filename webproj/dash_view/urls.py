from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "dash_view"

urlpatterns = [
    path("", views.page_fileupload, name = "uploadFile"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )