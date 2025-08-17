from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_1view, name='app_1'),

]
