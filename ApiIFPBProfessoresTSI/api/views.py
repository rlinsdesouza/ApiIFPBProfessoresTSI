from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from .models import Professor
from .serializers import ProfessorSerializer


# Create your views here.

class ProfessorViewSet(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
