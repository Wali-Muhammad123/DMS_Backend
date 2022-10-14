from django.shortcuts import render
import json
from django.http import JsonResponse
def api_initial(request,*args,**kwargs):
    data={
        'name':'Django',
        'version':'3.2.5'
    }
    return JsonResponse(data)
# Create your views here.
