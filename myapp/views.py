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
        a=data["a"]
        b=data["b"]
        res = {"data":0}
        serializer = add(data=data) 
        if serializer.is_valid():
            c=a+b
            res["data"]=c
            #json_obj= json.loads(str(res))
            return JsonResponse(res)
            #return HttpResponse(c)
        return JsonResponse(serializer.errors,status=400)