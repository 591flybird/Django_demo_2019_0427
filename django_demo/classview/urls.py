# _*_ coding:utf-8 _*_
from django.conf.urls import url

__author__ = 'hjl'
__date__ = '19-1-10 下午8:21'
from . import views
urlpatterns = [
    url(r'^index1/$', views.index,name='index'),
    url(r'^get_post/$',views.classview.as_view())
]
