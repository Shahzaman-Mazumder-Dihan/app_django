from django.shortcuts import render

# Create your views here.


def app_1view(request):
    return render(request, 'app_1/app_1.html')
