from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("""
    <html>
    <head>
    <title>MyProject</title>
    </head>
    
    <body>
    <h1>Hello World</h1>
    </body>
    
    
    </html>
    
    """)


def root_page(request):
    return render(request, template_name="myapp/root_page.html")


def temp_inherit_home(request):
    return render(request, template_name="myapp/temp_inherit_home.html")


def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")
