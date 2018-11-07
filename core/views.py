from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'mensagem':'Olá mundo'}
    return render(request , 'core/index.html', context)