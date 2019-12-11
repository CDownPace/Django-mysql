from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Avg
from django.db import connection
# Create your views here.


def index(request):
    # 获取所有图书的定价的平均价
    result=Book.objects.aggregate(my_avg=Avg('price'))
    print(result)
    # query 通过query可以看到语句被转换成sql语句后的样子
    # print(result.query)
    print(connection.queries)
    return HttpResponse("index")