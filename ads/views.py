from django.http import JsonResponse
from django.shortcuts import render


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)