from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from django.db.models import Q,F,Count
from django.db import connection
# 用于取反操作

from django.db.models.query import QuerySet
from django.db.models.manager import Manager
# Create your views here.
def index(request):
    print(type(Book.objects))
    return HttpResponse('index')

def index2(request):
    # books=Book.objects.filter(id__gte=2)
    # books = Book.objects.exclude(id__gte=2)
    # books=books.filter(~Q(id=3))
    # for book in books:
    #     print(book)
    books=Book.objects.annotate(author_name=F("author"))
    for book in books:
        print('%s/%s'%(book.name,book.author_name))
        # print(connection.queries)
    return HttpResponse('index2')


def index3(request):
    # 根据create_time从小到大进行排序
    # orders=BookOrder.object.order_by("create_time")

    # 根据create_time从大到小进行排序
    orders = BookOrder.object.order_by("-create_time")
    for order in orders:
        print("%s/%s"%(order.id,order.create_time))

    # 提取图书数据:聚合函数，根据图书的销量进行排序（从大到小排序）
    # books=Book.objects.annotate(order_nums=Count("bookorder")).order_by('-order_nums')
    # for book in books:
    #     print('%s/%s'%(book.name,book.order_nums))
    return HttpResponse('index3')


