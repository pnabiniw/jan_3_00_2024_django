from django.shortcuts import render


def signup(request):
    return render(request, template_name="crud/signup.html")
