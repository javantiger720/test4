# _*_ coding:utf-8 _*_
from django.http import HttpResponse


# Create your views here.

def abc(request):
    return HttpResponse('hello 你好！,我是正式服务器')
