from django.urls import path
from .views import (
    ListView
)

urlpatterns = [
    path('', ListView, name="coffee-list")
]
