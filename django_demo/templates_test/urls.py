# _*_ coding:utf-8 _*_
from django.conf.urls import url
from . import views
__author__ = 'hjl'
__date__ = '19-4-26 下午8:09'

urlpatterns = [url(r'^templates/$',views.Templates_test.as_view()),
]