from . import views
from django.urls import path


urlpatterns = [
    # path('analysis/', views.analysis, name='analysis'),
    path('weblogs/',views.weblogs,name='weblogs'),
    path('webcount/',views.webcount,name='webcount'),
]