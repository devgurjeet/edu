from rest_framework import serializers
from universities.models import Universities


class UniversitiesSerializers(serializers.ModelSerializer):
    model = 'Universities'
