"""Platzi gram views"""

#Django
from django.http import HttpResponse

#Utilidades
from datetime import datetime
import json

def hello_word(request):
    """Retorna un texto"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hola, la hora del servidor es {now}'. format(now=now))

def numeros_ordenados(request):
    """Retornando numeros ordenados en Json"""
    aux = request.GET['numbers']
    numbers = [int(i) for i in aux.split(',')]
    sorted_ins = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ins,
        'message':'Numeros ordenados correctamente'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    """Retorna nombre y edad"""
    if age < 12:
        message = 'Sorry {}, no puedes estar aqui'.format(name)
    else:
        message = 'Hola, {}! Bienvenido a platzigram'.format(name)
        
    return HttpResponse(message)