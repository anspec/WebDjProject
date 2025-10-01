from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'caption': 'Сайт специалиста 1С'
    }
    return render(request, 'main/index.html', context)

def new(request):
    return render(request, 'main/new.html')


