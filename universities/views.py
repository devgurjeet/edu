from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from universities.models import Universities
from universities.serializers import UniversitiesSerializers


class UniversitiesListAPIView(ListAPIView):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializers
