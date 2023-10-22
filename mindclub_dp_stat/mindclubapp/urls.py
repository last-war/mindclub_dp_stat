from django.urls import path
from . import views

app_name = 'mindclubapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('season/', views.season, name='season'),
    path('gametype/', views.gametype, name='gametype'),
]
