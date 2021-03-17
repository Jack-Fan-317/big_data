from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
# Create your views here.
from .models import WeblogsSmall,WebCount,Weblogs
from django.db import connection
from collections import namedtuple


# 生成列表对象方法
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


# 生成字典方法
def dictfetchall(cursor):
    # columns = [col[0] for col in cursor.description]
    columns = ['name','value']
    print(columns)
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# 日志累计采集数量情况
# weblogsTotal
def weblogsTotal(request):
    with connection.cursor() as cursor:
        cursor.execute("select count(*) from myapp_Weblogs")
        row_total = cursor.fetchall()
    return JsonResponse({
        "data": row_total[0][0]
    })


# 轮播图
# weblogsShow
def weblogsShow(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from myapp_WeblogsSmall limit 500")
        row = namedtuplefetchall(cursor)
        result_rows = []
        for i in range(len(row)):
            result_rows.append([row[i].datatime,row[i].userid,row[i].retorder,row[i].cliorder])
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



# 话题TOP50
# weblogsTopic
def weblogsTopic(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from myapp_WebCount limit 50")
        row = dictfetchall(cursor)
    return JsonResponse({
        "data":{
            "data":row,
            "rowNum": 10,
            "waitTime": 2000
        },
    })


# 累计web日志时间分布
# timeDistrib
def timeDistrib(request):
    with connection.cursor() as cursor:
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '00:00:00.000' and datatime < '03:00:00.000'")
        row_0_3 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '03:00:00.000' and datatime < '06:00:00.000'")
        row_3_6 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '06:00:00.000' and datatime < '09:00:00.000'")
        row_6_9 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '09:00:00.000' and datatime < '12:00:00.000'")
        row_9_12 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '12:00:00.000' and datatime < '15:00:00.000'")
        row_12_15 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '15:00:00.000' and datatime < '18:00:00.000'")
        row_15_18 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '18:00:00.000' and datatime < '21:00:00.000'")
        row_18_21 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '21:00:00.000' and datatime < '24:00:00.000'")
        row_21_24 = cursor.fetchall()
    return JsonResponse({
        "data": {
            "data": [
                {
                    'name': '00:00-03:00',
                    'value': row_0_3[0][0]
                },
                {
                    'name': '03:00-06:00',
                    'value': row_3_6[0][0]
                },
                {
                    'name': '06:00-09:00',
                    'value': row_6_9[0][0]
                },
                {
                    'name': '09:00-12:00',
                    'value': row_9_12[0][0]
                },
                {
                    'name': '12:00-15:00',
                    'value': row_12_15[0][0]
                },
                {
                    'name': '15:00-18:00',
                    'value': row_15_18[0][0]
                },
                {
                    'name': '18:00-21:00',
                    'value': row_18_21[0][0]
                },
                {
                    'name': '21:00-24:00',
                    'value': row_21_24[0][0]
                }
            ],
            'unit': '条'
        }
    })


# 4图
# timeItems
def timeItems(request):
    with connection.cursor() as cursor:
        # 0-6
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '00:00:00.000' and datatime < '01:00:00.000'")
        row_0_1 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '01:00:00.000' and datatime < '02:00:00.000'")
        row_1_2 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '02:00:00.000' and datatime < '03:00:00.000'")
        row_2_3 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '03:00:00.000' and datatime < '04:00:00.000'")
        row_3_4 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '04:00:00.000' and datatime < '05:00:00.000'")
        row_4_5 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '05:00:00.000' and datatime < '06:00:00.000'")
        row_5_6 = cursor.fetchall()
        # 6-12
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '06:00:00.000' and datatime < '07:00:00.000'")
        row_6_7 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '07:00:00.000' and datatime < '08:00:00.000'")
        row_7_8 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '08:00:00.000' and datatime < '09:00:00.000'")
        row_8_9 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '09:00:00.000' and datatime < '10:00:00.000'")
        row_9_10 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '10:00:00.000' and datatime < '11:00:00.000'")
        row_10_11 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '11:00:00.000' and datatime < '12:00:00.000'")
        row_11_12 = cursor.fetchall()
        # 12-18
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '12:00:00.000' and datatime < '13:00:00.000'")
        row_12_13 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '13:00:00.000' and datatime < '14:00:00.000'")
        row_13_14 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '14:00:00.000' and datatime < '15:00:00.000'")
        row_14_15 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '15:00:00.000' and datatime < '16:00:00.000'")
        row_15_16 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '16:00:00.000' and datatime < '17:00:00.000'")
        row_16_17 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '17:00:00.000' and datatime < '18:00:00.000'")
        row_17_18 = cursor.fetchall()
        # 18-24
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '18:00:00.000' and datatime < '19:00:00.000'")
        row_18_19 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '19:00:00.000' and datatime < '20:00:00.000'")
        row_19_20 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '20:00:00.000' and datatime < '21:00:00.000'")
        row_20_21 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '21:00:00.000' and datatime < '22:00:00.000'")
        row_21_22 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '22:00:00.000' and datatime < '23:00:00.000'")
        row_22_23 = cursor.fetchall()
        cursor.execute("select count(*) from myapp_Weblogs where datatime >= '23:00:00.000' and datatime < '24:00:00.000'")
        row_23_24 = cursor.fetchall()
        
    return JsonResponse({
        "data1": {
            "title": {
                'text':'日志量',
                'style':{
                    'fill': '#eee',
                    'fontSize': 17,
                    'fontWeight': '400',
                    'textAlign': 'center',
                    'textBaseline': 'bottom',
                },
            },
            'xAxis': {
                'name': '时',
                'data': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'yAxis': {
                'name': '条',
                'data': 'value',
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'series': [
                {
                    'data': [row_0_1[0][0],row_1_2[0][0],row_2_3[0][0],row_3_4[0][0],row_4_5[0][0],row_5_6[0][0]],
                    'type': 'bar',
                    'gradient': {
                        'color': ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
                    },
                    'barStyle': {
                        'stroke': '#fb7293'
                    }
                }
            ],
        },
        "data2": {
            "title": {
                'text':'日志量',
                'style':{
                    'fill': '#eee',
                    'fontSize': 17,
                    'fontWeight': '400',
                    'textAlign': 'center',
                    'textBaseline': 'bottom',
                },
            },
            'xAxis': {
                'name': '时',
                'data': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'yAxis': {
                'name': '条',
                'data': 'value',
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'series': [
                {
                    'data': [row_6_7[0][0],row_7_8[0][0],row_8_9[0][0],row_9_10[0][0],row_10_11[0][0],row_11_12[0][0]],
                    'type': 'bar',
                    'gradient': {
                        'color': ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
                    },
                    'barStyle': {
                        'stroke': '#fb7293'
                    }
                }
            ],
        },
        "data3": {
            "title": {
                'text':'日志量',
                'style':{
                    'fill': '#eee',
                    'fontSize': 17,
                    'fontWeight': '400',
                    'textAlign': 'center',
                    'textBaseline': 'bottom',
                },
            },
            'xAxis': {
                'name': '时',
                'data': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'yAxis': {
                'name': '条',
                'data': 'value',
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'series': [
                {
                    'data': [row_12_13[0][0],row_13_14[0][0],row_14_15[0][0],row_15_16[0][0],row_16_17[0][0],row_17_18[0][0]],
                    'type': 'bar',
                    'gradient': {
                        'color': ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
                    },
                    'barStyle': {
                        'stroke': '#fb7293'
                    }
                }
            ],
        },
        "data4": {
            "title": {
                'text':'日志量',
                'style':{
                    'fill': '#eee',
                    'fontSize': 17,
                    'fontWeight': '400',
                    'textAlign': 'center',
                    'textBaseline': 'bottom',
                },
            },
            'xAxis': {
                'name': '时',
                'data': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'yAxis': {
                'name': '条',
                'data': 'value',
                'nameTextStyle': {
                    'fill': '#fff',
                    'fontSize': 10
                },
                'axisLabel':{
                    'style': {
                        'fill': '#fff',
                        'fontSize': 10,
                        'rotate': 0
                    }
                },
            },
            'series': [
                {
                    'data': [row_18_19[0][0],row_19_20[0][0],row_20_21[0][0],row_21_22[0][0],row_22_23[0][0],row_23_24[0][0]],
                    'type': 'bar',
                    'gradient': {
                        'color': ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
                    },
                    'barStyle': {
                        'stroke': '#fb7293'
                    }
                }
            ],
        }
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