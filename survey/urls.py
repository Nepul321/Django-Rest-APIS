from django.urls import path

from survey.views import submission_create, submissions_list

urlpatterns = [
    path('', submissions_list, name="submissions-list"),
    path('create/', submission_create, name="submission-create"),
]
