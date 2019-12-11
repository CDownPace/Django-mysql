from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.
def index(request):
#     1.使用ORM添加一条数据到数据库中
#     book=Book(name='西游记',author='吴承恩',price=200)
#     book.save()

    # 2.查询

    # 2.1.根据主键进行查找
    #  pk表示主键 primary key
    book=Book.objects.get(pk=2)
    print(book)
    return HttpResponse("图书添加成功")


    # 2.2根据其他条件进行查找
    # books=Book.objects.filter(name='西游记')
    # print(books)

    # 3.删除数据
    # book=Book.objects.get(pk=1)
    # book.delete()

    # 4.修改数据
    # book=Book.objects.get(pk=2)
    # book.price=200
    # book.save()
    # return HttpResponse('图书修改成功')

