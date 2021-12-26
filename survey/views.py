from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    SubmissionSerializer
)
from survey.models import Submission

@api_view(['GET'])
def submissions_list(request):
    qs = Submission.objects.all()
    serializer = SubmissionSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['POST'])
def submission_create(request):
    data = request.data
    serializer = SubmissionSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"message" : "Thanks for taking the survey"}, status=201)
    return Response({"message" : "An error occurred"}, status=500)