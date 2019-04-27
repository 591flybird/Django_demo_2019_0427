import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse


def index(request):
    print(reverse('users:index'))  # 可以直接去导入reverse函数
    return HttpResponse('haha')  # 也可以直接导入



def test(request):
    print(reverse('haha'))  # 反向解析url
    return HttpResponse('test')


def get_agrs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.getlist('c')
    print(a)
    print(b)
    print(c)

    return HttpResponse('ok')


def re_test(request, name, age):
    # 正则匹配ｕｒｌ
    print(name)
    print(age)

    return HttpResponse('ok')


def weather(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('OK')


def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')


def get_body_json(request):
    # 提取非表单数据的json
    json_str = request.body  # 获取的是字节流
    json_str = json_str.decode()
    dict_str = json.loads(json_str)  # python3.6以上可以直接传字节流
    print(dict_str)
    return HttpResponse('ok')


def get_headers(request):
    dict = request.META
    print(dict['CONTENT_TYPE'])
    print(request.method)  # 获取请求方式
    print(request.user)  # 查看用户对象
    print(request.path)  # 不包含域名和参数的请求路径
    print(request.encoding)  # 查看编码，如果为None则表示使用浏览器的默认设置，一般为utf-8
    print(request.FILES)  # 查看上传的文件

    return HttpResponse('OK')


def get_response(request):
    # 方式1 直接构造响应对象，内容＋类型＋状态码
    response = HttpResponse(content='str', content_type='str', status=200)
    # 方式２  根据属性设置
    # content：表示返回的内容。
    # status_code：返回的HTTP响应状态码。
    # content_type：指定返回数据的的MIME类型。
    response2 = HttpResponse('哈哈哈')
    response2['head1'] = 'hjl'  # 自定义响应头
    response2['head2'] = 'hjl2'
    response2.status_code = 200
    # 方式３　　返回json数据
    response3 = JsonResponse({'a': 1, 'b': 2})  # 直接将字典类型转为json类型，作为响应内容发送给浏览器
    # 方式4 redirect 重定向，需要导包
    return redirect(reverse('haha'))


def get_cookies(request):
    # 获取cookies
    # cookie1 = request.COOKIES
    # print(cookie1)
    # return HttpResponse('OK')
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')  # 临时cookie
    response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
    return response


def get_sessions(request):
    print(request.session.get('name'))
    # request.session['name'] = 'hjl'
    # request.session['name'] = 'cl'
    # request.session.set_expiry(0) # 设置过期时间,单位为秒,不写默认是２周，０表示临时session
    '''
    2）根据键读取值。
    # request.session.get('键',默认值)
    3）清除所有session，在存储中删除值部分。
    request.session.clear()
    4）清除session数据，在存储中删除session的整条数据。
    request.session.flush()
    5）删除session中的指定键及值，在存储中只删除某个键及对应的值。
    del request.session['键']
    '''

    return HttpResponse('ok', status=200)
