from django.shortcuts import render, HttpResponse
from django.core import serializers

from . import models

from django.http import JsonResponse

from django.db.models import Q

# Create your views here.


def index(request):
    return render(request, "index.html")


def page_dashboard(request):
    return render(request, "dashboard.html")


def api_notify(request):
    #content = list(models.Noti.objects.all().order_by('-id').values()) # 내림차순
    #return JsonResponse({'content': content})    
    content = models.Noti.objects.all().order_by('-id')[:5]
    content_list = serializers.serialize('json', content)
    return HttpResponse(content_list, content_type="text/json-comment-filtered")
    # return render(request, "", {'content': content})


def api_notifySelect(request):
    # q = Q()
    # q.add(Q(id=request.GET['id']))
    content = models.Noti.objects.filter(id=request.GET['id'])
    content_list = serializers.serialize('json', content)
    return HttpResponse(content_list, content_type="text/json-comment-filtered") 

def page_reports(request):
    itemlist = models.DetectedItem.objects.all()  # 여기서 오류남
    return render(request, "reports.html", {'itemlist': itemlist})
    # return render(request, "reports.html")


def page_fileupload(request):
    return render(request, "fileupload.html")


def error_401(request):
    return render(request, "401.html")


def error_404(request):
    return render(request, "404.html")


def error_500(request):
    return render(request, "500.html")


def page_charts(request):
    return render(request, "charts.html")


def page_layout_sidenav_light(request):
    return render(request, "layout-sidenav-light.html")


def page_layout_static(request):
    return render(request, "layout-static.html")


def page_login(request):
    return render(request, "login.html")


def page_password(request):
    return render(request, "password.html")


def page_register(request):
    return render(request, "register.html")


def page_tables(request):
    return render(request, "tables.html")
