from . import views
from django.urls import path

app_name = 'madlib'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:madlibId>', views.game, name='game'),
]