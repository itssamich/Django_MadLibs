from . import views
from django.urls import path

app_name = 'madlib'

urlpatterns = [
    path('', views.index, name='index'),
]