from . import views
from django.urls import path


urlpatterns = [
    path('weblogsShow/',views.weblogsShow,name='weblogsShow'),
    path('weblogsTopic/',views.weblogsTopic,name='weblogsTopic'),
    path('weblogsTotal/',views.weblogsTotal,name='weblogsTotal'),
    path('timeDistrib/',views.timeDistrib,name='timeDistrib'),
    path('timeItems/',views.timeItems,name='timeItems')
]