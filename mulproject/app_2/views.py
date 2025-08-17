from django.shortcuts import render

# Create your views here.


def app_2view(request):
    return render(request, 'app_2/app_2.html')
