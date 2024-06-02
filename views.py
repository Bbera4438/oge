from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',

    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def subjects(request):
    return render(request, 'main/subjects.html')

def informatic(request):
    return render(request, 'main/informatic.html')

def physic(request):
    return render(request, 'main/physic.html')

def math(request):
    return render(request, 'main/math.html')