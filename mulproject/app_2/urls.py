from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_2view, name='app_2'),

]
