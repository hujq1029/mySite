from django.conf.urls import include, url
from app01 import views

urlpatterns = [
    url(r'index',views.index)
]