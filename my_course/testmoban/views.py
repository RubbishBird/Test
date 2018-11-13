from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def login(request):
    next = request.GET.get('next')
    text = '登录页面，登录完成需要跳转的页面是： %s' % next
    return HttpResponse(text)

def book(request):
    return HttpResponse('这是读书页')

def book_detail(request,book_id):
    text = "图书的ID是: %s" % book_id
    return HttpResponse(text)

def movie(request):
    return HttpResponse("这是电影页")

def city(request):
    return HttpResponse("这是电影页")