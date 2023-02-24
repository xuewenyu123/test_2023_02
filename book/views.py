from django.shortcuts import render
from django.http import HttpResponse

from book.models import BookInfo
# Create your views here.

def create_book(request):
    book = BookInfo.objects.create(
        name = "abc",
        pub_date = "2000-1-1",
        readcount = 10,
    )
    return HttpResponse("ok")

def shop(request, city_id, mobile):
    print(city_id, mobile)
    return HttpResponse("欢迎！")


def register(request):

    data = request.POST['username']  # 接受post中Form表单的数据 
    print(data)
    return HttpResponse('ok')


def json(request):

    body = request.body  # 接受POST中传递的json格式的数据
    # b'{\n\t\t"name": "xue",\n \t\t"age": 20\n}'  输出为byte类型
    body_str = body.decode()
    print(body_str)
    print(request.META)  # 请求信息
    return HttpResponse("ok")


def method(request):

    print(request.method)
    return HttpResponse("method")


################查询字符串####################
"""
查询字符串
http://ip:port/path/path?key1=value1&key2=value2...

?前边为 请求路径
?后边为 查询字符串

request.GET  获取查询字符串的信息  返回 <QueryDict {"key1"={"value1"}}>

"""