from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class Accounts(View):
    def get(self, request):
        return JsonResponse([], safe=False)

    def post(self, request):
        return JsonResponse([], safe=False)