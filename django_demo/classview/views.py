from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):

    return HttpResponse('haha')

#　引入类视图

class classview(View):
    def post(self,request):
        return HttpResponse('这是post请求')
    def get(self,request):
        return HttpResponse('这是get请求')

