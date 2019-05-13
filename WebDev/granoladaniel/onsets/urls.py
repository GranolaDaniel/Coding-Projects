from django.urls import path

from . import views

app_name = 'onsets'
urlpatterns = [
    path('', views.index, name='index'),
    
]