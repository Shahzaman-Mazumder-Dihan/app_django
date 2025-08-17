
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('app1/', include('app_1.urls')),
    path('app2/', include('app_2.urls')),
    path('app3/', include('app_3.urls')),
]
