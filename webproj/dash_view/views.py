from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

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