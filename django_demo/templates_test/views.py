from django.shortcuts import render

# Create your views here.
from django.views import View


class Templates_test(View):
    def get(self, request):
        a = {'a':'hjl'}
        return render(request, 'TemplatesIndex.html', a)

    def post(self, request):
        a = {'a':'hjl22222'}
        return render(request, 'TemplatesIndex.html', a)
