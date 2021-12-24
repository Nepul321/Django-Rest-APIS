# from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import (
    Response
)
from rest_framework.decorators import (
    api_view
)
from .serializers import (
    CoffeeSerializer
)
from .models import (
    Coffee
)

@api_view(['GET'])
def ListView(request):
    qs = Coffee.objects.all()
    serializer = CoffeeSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)