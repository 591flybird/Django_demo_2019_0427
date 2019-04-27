from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户模块' # admin站点可以识别此字段，相当于起别名
