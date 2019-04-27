# _*_ coding:utf-8 _*_
__author__ = 'hjl'
__date__ = '19-1-9 下午10:37'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/', views.index,name='index'),
]
