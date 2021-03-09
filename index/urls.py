from . import views
from django.urls import path


urlpatterns = [
    # path('analysis/', views.analysis, name='analysis'),
    path('city/',views.cityData,name='cityData'),
]