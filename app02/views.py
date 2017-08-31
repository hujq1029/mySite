from django.shortcuts import render, HttpResponse
from app02 import models


# Create your views here.


def index(request):
    obj = models.UserInfo(username='tom', password='tom123')
    obj.save()

    return HttpResponse('app02ok')