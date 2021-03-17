from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
# Create your views here.
from .models import WeblogsSmall,WebCount
from django.db import connection
from collections import namedtuple


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def weblogs(request):
    # weblogs_all = WeblogsSmall.objects.all()
    # list_weblogs_all = []
    # for i in weblogs_all:
    #     list_weblogs = [i.datatime,i.userid,i.retorder,i.cliorder]
    #     list_weblogs_all.append(list_weblogs)
    #     list_weblogs = []
    with connection.cursor() as cursor:
        cursor.execute("select * from myapp_WeblogsSmall limit 500")
        row = namedtuplefetchall(cursor)
        result_rows = []
        for i in range(len(row)):
            result_rows.append([row[i].datatime,row[i].userid,row[i].retorder,row[i].cliorder])
        # print(result_rows)
    return JsonResponse({
        "data":{
            "header": ['时间', '用户ID', 'url排名', '顺序号'],
            "data":result_rows,
            "index": True,
            "carousel": 'page',
            "columnWidth": [100,170,230,100],
            "align": ['center'],
            "rowNum": 7,
            "headerBGC": '#1981f6',
            "headerHeight": 35,
            "oddRowBGC": 'rgba(0, 44, 81, 0.8)',
            "evenRowBGC": 'rgba(10, 29, 50, 0.8)'
        },
    })
# raw方法
    # test = WeblogsSmall.objects.raw('select * from myapp_WeblogsSmall')[0]
    # print(test.userid)

    # cursor方法
    # with connection.cursor() as cursor:
    #     cursor.execute("select count(*) from myapp_WeblogsSmall")
    #     row = cursor.fetchone()
    # print(row[0])

    # with connection.cursor() as cursor:
    #     cursor.execute("select * from myapp_WeblogsSmall")
    #     row = cursor.fetchall()
    #     for i in range(10):
    #         print(row[i])

def dictfetchall(cursor):
    # columns = [col[0] for col in cursor.description]
    columns = ['name','value']
    print(columns)
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def webcount(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from myapp_WebCount limit 50")
        # row = cursor.fetchall()
        row = dictfetchall(cursor)
        # print(row)
    return JsonResponse({
        "data":{
            "data":row,
            "rowNum": 10,
            "waitTime": 2000
        },
    })