## first部分
```python
from django.shortcuts import render

from django.db import connection
def index(request):
    cursor=connection.cursor()
    # 连接数据库
    # 添加数据库
    # cursor.execute("insert into book(id,name,author) values(null,'西游记','吴承恩')")
    # 查找数据库
    cursor.execute("select id,name,author from book")
    rows=cursor.fetchall()
    # fetchall   返回所有的数据
    # fetchone  返回一条数据
    # fetchamany(5)  指定返回5条数据
    for row in rows:
        print(row)
    return render(request,'index.html')
```


## three_orm_test部分

```python
from django.db import models

# Create your models here.
# 如果要将一个普通的类变成一个可以映射到数据库中的ORM模型，那么必须要将父类设置为models.Model或者其他的子类
class Book(models.Model):
    # 1.id:int类型，是自增长的。autoField表示自动增长。primary_key=True表示主键
    id=models.AutoField(primary_key=True)
    # 2.name:varchar(100),图书的名字
    name=models.CharField(max_length=100,null=False)
    # 3.author:varchar(100),图书的作者   不能为空
    author = models.CharField(max_length=100, null=False)
    # 4.price:float,图书的价格    默认值为0
    price=models.FloatField(null=False,default=0)


# 如果没有创建id。它会自动创建
class Publisher(models.Model):
    name=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100,null=False)

# 1.使用makemigrations生成迁移脚本文件
# python manage.py makemigrations

# 2.使用将新生成的迁移脚本文件映射到数据库中
# python manage.py migrate
```


## three_orm2_test部分
```python
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

```


## five部分
> exact：使用精确的 = 进行查找。如果提供的是一个 None ，那么在 SQL 层面就是被解释为 NULL 。
```
article = Article.objects.get(id__exact=14) 
article = Article.objects.get(id__exact=None)
```
相当于：
```
select ... from article where id=14; 
select ... from article where id IS NULL;
```

> iexact：使用like进行查找
```
article=Article.objects.filter(title_iexact='hello world')
```
相当于:
```
select ...from article where title like 'hello world';
```
> contains：大小写敏感，判断某个字段是否包含了某个数据。

```
articles = Article.objects.filter(title__contains='hello')
```
在翻译成 SQL 语句
```
select ... where title like binary '%hello%';
```
要注意的是，在使用 contains 的时候，翻译成的 sql 语句左右两边是有百分号的，意味着使用 的是模糊查询。而 exact 翻译成 sql 语句左右两边是没有百分号的，意味着使用的是精确的查 询

> icontains：大小写不敏感的匹配查询。
```
articles = Article.objects.filter(title__icontains='hello')
```
在翻译成 SQL 语句
```
select ... where title like '%hello%';
```

## six聚合函数部分
> 聚合函数是对数据进行提取并进行一些处理。比如售出商品的平均价格。聚合函数是通过 aggregate 方法来实现的


