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