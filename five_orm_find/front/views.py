from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def index(request):
    article=Article.objects.get(id__exact=1)
    print(article)
    return HttpResponse("success")

def index1(request):
    article=Article.objects.get(pk=1)
    print(type(article))
    return HttpResponse("success")

def index2(request):
    # contains 使用大小写敏感的判断，某个字符串是否在指定的字符中，这个判断条件会使用大小写敏感，
    # 因此，被翻译成‘sql’语句的时候，会使用‘like binary’，而‘like binary’就是使用大小写敏感的
    # icontains 忽略大小写
    result=Article.objects.filter(title_contains='hello')
    print(request.query)
    print(result)
    return HttpResponse('success')