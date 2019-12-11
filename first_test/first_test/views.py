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