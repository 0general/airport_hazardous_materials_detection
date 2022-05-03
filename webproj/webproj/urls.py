"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from dash_view.views import index, error_401, error_404, error_500, page_charts, page_layout_sidenav_light,\
                       page_layout_static, page_login, page_password, page_register, page_tables, \
                       page_dashboard, page_reports, page_fileupload, api_notify, api_notifySelect
urlpatterns = [
    path('', index),
    path('error_401/', error_401),
    path('error_404/', error_404),
    path('error_500/', error_500),
    path('page_charts/', page_charts),
    path('page_layout_sidenav_light/', page_layout_sidenav_light),
    path('page_layout_static/', page_layout_static),
    path('page_login/', page_login),
    path('page_password/', page_password),
    path('page_register/', page_register),
    path('page_tables/', page_tables),
    path('page_dashboard/', page_dashboard),
    path('api_notify/', api_notify, name='api_notify'),
    path('api_notifySelect/', api_notifySelect, name='api_notifySelect'),
    path('page_reports/', page_reports),
    path('page_fileupload/', page_fileupload),
    path("", include("dash_view.urls")),
    path('admin/', admin.site.urls),
]
