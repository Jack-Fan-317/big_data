from . import views
from django.urls import path


urlpatterns = [
    # path('analysis/', views.analysis, name='analysis'),
    path('city1/',views.cityData1,name='cityData'),
    path('city2/',views.cityData2,name='cityData'),
]