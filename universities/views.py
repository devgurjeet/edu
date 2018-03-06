from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from universities.serializers import UniversitiesSerializers
@api_view()
def hello(request):
    return Response({"message": "Hello, world!"})


class Universities(GenericAPIView):
    serializer_class = UniversitiesSerializers

    def get(self):
        pass

