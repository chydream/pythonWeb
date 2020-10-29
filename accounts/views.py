from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie


class Accounts(View):
    def get(self, request):
        return JsonResponse([], safe=False)

    @ensure_csrf_cookie
    def post(self, request):
        return JsonResponse([], safe=False)