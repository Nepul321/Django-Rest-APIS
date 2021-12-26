from django.urls import path

from survey.views import submissions_list

urlpatterns = [
    path('', submissions_list, name="submissions-list"),
]
