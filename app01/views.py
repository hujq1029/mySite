from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.


def index(request):
    obj = models.UserInfo(username='jack',password='jack123')
    obj.save()
    return HttpResponse('app01ok')