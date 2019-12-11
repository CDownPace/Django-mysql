from django.shortcuts import render
from .models import Category,Article
from django.http import HttpResponse
# Create your views here.
def index(request):
    # category = Category(name='最新文章')
    # category.save()
    # article = Article(title='abc', content='111')
    # article.category=category
    # article.save()

    article=Article.objects.first()
    print(article.category.name)
    # 查找最新文章的那条数据
    return HttpResponse('success')

def one_to_many_view(request):
    # 1.一对多的关联操作
    # article=Article(title="钢铁是怎样炼成的",content='abc')
    # category=Category.objects.first()
    # # author=FrontUser.objects.first()
    # article.category=category
    # article.save()
    # return HttpResponse('success')

    # 2.获取某个分类上所有的文章
    category=Category.objects.first()
    # article=category.article_set.all()
    # # article = category.article.all()
    # for article in article:
    #     print(article)

    article=Article(title='111',content='222')
    # article.author=FrontUser.objects.first()
    # category.save()
    # article.category=category
    # category.articles.add(article)
    # category.save()
    return HttpResponse("success")
