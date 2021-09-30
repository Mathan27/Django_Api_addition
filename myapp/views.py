import json
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from myapp.serializers import add
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def addition(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        d= dict(data)
        res = {"data":0}
        s=0
        for key,value in d.items():
            if(int == type(value)):
                s=s+value
        res["data"]=s
        return JsonResponse(res)