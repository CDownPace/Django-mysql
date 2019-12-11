from django.db import models

# Create your models here.
# 分类的模型
class Category(models.Model):
    name=models.CharField(max_length=100)

# app.模型的名字

class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ForeignKey("Category",on_delete=models.CASCADE)
    author=models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE,
null=True,related_name="article")
    # related_name="articles"相当于article_set

    def _str_(self):
        return "<Article:(id:%s,title:%s)>"%(self.id,self.title)

# 引用自身
class Comment(models.Model):
    content=models.TextField()
    origin_comment=models.ForeignKey("self",on_delete=models.CASCADE)