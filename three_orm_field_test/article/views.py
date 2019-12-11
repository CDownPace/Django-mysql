from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Person
# Create your views here.
from .models import Article
def index(request):
    # article=Article(removed=False)
    # article.save()

    return HttpResponse('success')


def email_view(request):
    # pass
    p= Person (email='xxx@qq.com')
    p.save()
    # emailField在数据库层面并不会限制字符串一定要满足邮箱格式
    # 只是以后在使用ModelForm等表单相关操作的时候会起作用
    return HttpResponse('success')