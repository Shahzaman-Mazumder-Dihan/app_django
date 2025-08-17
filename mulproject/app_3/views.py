from django.shortcuts import render

# Create your views here.


def app_3view(request):
    return render(request, 'app_3/app_3.html')
