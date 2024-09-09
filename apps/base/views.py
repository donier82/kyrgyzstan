from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('hello world')

# def about(request):
#     text="Мы создаем экосистему для обучение, работы и IT-специалистов"
#     return HttpResponse (text)

def index(request):
    return render(request, 'index.html')

def about(request):
    text={
        'title': 'О нас',
        'description': "Мы создаем экосистему для обучение, работы и IT-специалистов",
        'students':['ergashov donier','umaraliev aknazar','abdimitalipov janbolot','mitalipov azatbek','alisher talantbek','saydarov azamhoja','idirisov abduazim']
    }
    return render(request, 'about.html', text)