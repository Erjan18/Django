from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def generate_secret():
    x = random.sample([1,2,3,4,5,6,7,8,9,0],4)
    return x

def count_bulls(answer,quess):
    bulls = 0
    i = 0
    while i <len(quess):
        if quess[i] == answer[i]:
            bulls +=1
        i = i + 1
    return bulls

def count_cows(answer,quess):
    cows = 0
    i = 0
    while i < len(quess):
        if quess in answer:
            cows +=1
        i = i + 1
    return cows

def final(request):
    answer = generate_secret()
    quess = [2,3,1,4]
    bulls = count_bulls(answer,quess)
    cows = count_bulls(answer,quess)
    return render(request, 'ttp/hi.html',{'bulls':bulls,'cows':cows})