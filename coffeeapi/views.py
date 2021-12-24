from django.shortcuts import render
from django.http import JsonResponse

def ListView(request):
    return JsonResponse({'message' : 'Plain django'})