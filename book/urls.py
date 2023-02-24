from django.urls import path
from django.urls.converters import register_converter

from book.views import create_book, shop, register, json, method


# 1.定义转换器
class MobileConverter:
    # 验证数据
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     # 将匹配结果用于反向解析传值时使用
    #     return value

# 2.注册转换器, 注册之后才可以使用
register_converter(MobileConverter, "phone")


urlpatterns = [
    path('create/', create_book),
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
]