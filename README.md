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
> Avg ：求平均值。比如想要获取所有图书的价格平均值。那么可以使用以下代码实现。
```python
from django.db.models import Avg
result = Book.objects.aggregate(Avg('price'))
print(result)
# 以上的打印结果是：
{"price__avg":23.0}
```
```python
# 其中 price__avg 的结构是根据 field__avg 规则构成的。如果想要修改默认的名字，那么可以将 Avg 赋值给一个关键字参数。示例代码如下：
from django.db.models import Avg
result = Book.objects.aggregate(my_avg=Avg('price'))
print(result)
# 那么以上的结果打印为：
{"my_avg":23}
```
> Count ：获取指定的对象的个数。示例代码如下：
```python
from django.db.models import Count
result = Book.objects.aggregate(book_num=Count('id'))
#以上的 result 将返回 Book 表中总共有多少本图书。
```
```python
#Count 类中，还有另外一个参数叫做 distinct ，默认是等于 False ，如果是等于 True ，那么将去掉那些重复的值。比如要获取作者表中所有的不重复的邮箱总共有多少个，那么可以通过以下代码来实现：
from djang.db.models import Count
66result = Author.objects.aggregate(count=Count('email',distinct=True))
```
> Max 和 Min ：获取指定对象的最大值和最小值。
```python
#比如想要获取 Author 表中，最大的年龄和最小的年龄分别是多少。那么可以通过以下代码来实现：
from django.db.models import Max,Min
result = Author.objects.aggregate(Max('age'),Min('age'))
#如果最大的年龄是88,最小的年龄是18。那么以上的result将为：
{"age__max":88,"age__min":18}
```
> Sum ：求指定对象的总和。比如要求图书的销售总额。那么可以使用以下代码实现：
```python
from djang.db.models import Sum
result = Book.objects.annotate(total=Sum("bookstore__price")).values("name","total"
)
#以上的代码 annotate 的意思是给 Book 表在查询的时候添加一个字段叫做 total ，这个字段的数据来源是从 BookStore 模型的 price 的总和而来。 values 方法是只提取 name 和 total 两个字段的值。
```

> aggregate和annotate的区别：
1. aggregate ：返回使用聚合函数后的字段和值。
2. annotate ：在原来模型字段的基础之上添加一个使用了聚合函数的字段，并且在使用聚合函
数的时候，会使用当前这个模型的主键进行分组（group by）。
比如以上 Sum 的例子，如果使用的是 annotate ，那么将在每条图书的数据上都添加一个字段
叫做 total ，计算这本书的销售总额。
而如果使用的是 aggregate ，那么将求所有图书的销售总额

> F表达式 是用来优化 ORM 操作数据库的。首先从数据库中提取数据到Python内存中，然后在Python内存中做完运算，之后再保存到数据库中。他可以直接执行 SQL语句 ，就将员工的工资增加1000元
```python
from djang.db.models import F
Employee.object.update(salary=F("salary")+1000)
```
```python
如果想要获取作者中， name 和 email 相同的作者数据。
from django.db.models import F
authors = Author.objects.filter(name=F("email"))
```

> Q表达式，如果想要实现一些复杂的查询语句，比如要查询所有价格低于10元，或者是评分低于9分的图书。那就没有办法通过传递多个条件进去实现了。
```python
from django.db.models import Q
books = Book.objects.filter(Q(price__lte=10) | Q(rating__lte=9))
```
```python
#以上是进行或运算，当然还可以进行其他的运算，比如有 & 和 ~（非） 等。一些用 Q 表达式的例
子如下：
from django.db.models import Q
# 获取id等于3的图书
books = Book.objects.filter(Q(id=3))
# 获取id等于3，或者名字中包含文字"记"的图书
books = Book.objects.filter(Q(id=3)|Q(name__contains("记")))
# 获取价格大于100，并且书名中包含"记"的图书
books = Book.objects.filter(Q(price__gte=100)&Q(name__contains("记")))
# 获取书名包含“记”，但是id不等于3的图书
books = Book.objects.filter(Q(name__contains='记') & ~Q(id=3))
```

## QuerySet API：
```python
# models部分
class Publisher(models.Model):
    """出版社模型"""
    name = models.CharField(max_length=300)
    class Meta:
        db_table = 'publisher'

class Book(models.Model):
    """图书模型"""
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    class Meta:
        db_table = 'book'

class BookOrder(models.Model):
    """图书订单模型"""
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    price = models.FloatField()
    class Meta:
        db_table = 'book_order'
        # ordering=['-create_time','price']
        
#views部分
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
```




