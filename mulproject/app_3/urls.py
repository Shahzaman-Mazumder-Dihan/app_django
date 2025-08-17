from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_3view, name='app_3'),

]
