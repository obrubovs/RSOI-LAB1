from django.shortcuts import render


# Create your views here.

def index(request):
    data = {
        'name': 'Vasya',
        'age': 23
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def persons(request):
    return render(request, 'main/about.html')
