from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projected_score/', views.projected_score, name='projected_score'),
    path('win_prediction/', views.win_prediction, name='win_prediction')
]