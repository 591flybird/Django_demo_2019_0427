"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 带斜线是为了用户访问时结尾路由不带斜线也可以访问，自动重定向
    url(r'', include('users.urls', namespace='users')),  # 指定命名空间
    url(r'', include('classview.urls')), # 类视图的使用
    url(r'^classview/', include('classview.urls')),  # 链接classview模块中的url（设置子路由）
    # url(r'^classview/$', include('classview.urls')),  # 这里有个bug，注意这里千万不能写上$，否则识别不了后面的子路由
    url(r'^user/$', views.test, name='haha'),  # 不通过子url直接访问．直接命名也可以反解析
    url(r'^get_args/$', views.get_agrs),  # 获取参数
    url(r'^re/([a-z]+)/(\d{4})/$', views.re_test),  # 正则匹配ｕｒｌ
    url(r'^weathe$', views.get_body),  # 使用post请求，获取请求体的内容，postman测试时，url尾部必须有／,表单数据
    url(r'^get_body_json/$', views.get_body_json),  # 提取json，非表单数据
    url(r'^get_headers/$', views.get_headers),  # 获取请求头的数据
    url(r'^get_response/$', views.get_response),  # 构建响应对象的测试
    url(r'^get_cookies/$', views.get_cookies),  # 设置，获取cookies的demo演示
    url(r'^get_session/$', views.get_sessions),  # 设置session的demo演示
    url(r'',include('templates_test.urls'))
]
