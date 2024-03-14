from django.http.response import JsonResponse


def home(request):
    return JsonResponse({
        "message": "I am learning APIs"
    })
