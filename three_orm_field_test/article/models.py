from django.db import models

# Create your models here.
class Article(models.Model):
    id=models.BigAutoField(primary_key=True)
    # primary_key=True  表示自定义主键
    # 添加的其实是一个字段
    # removed=models.BooleanField()
    # 删除数据之后数据库其实并未真正删除，通过这种方式告知客户数据已经删除
    # 添加了removed的字段

    # 如果想要使用可以为null的BooleanField,那应该使用nullBooleanField代替
    removed = models.NullBooleanField()

    title=models.CharField(max_length=200)

    create_time=models.DateTimeField(auto_now=True)
    # 创建时间
    # 更新时间
class Person(models.Model):
        # EmailField在数据库层面并不会限制字符串一定要满足邮箱格式
        # 只是以后在使用ModelForm等表单相关操作的时候会起作用
        email=models.EmailField()
        # 查看某部分是ctrl+b
        signature=models.TextField()
    #     可以存储任意大量文本类型
