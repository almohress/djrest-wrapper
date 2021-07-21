from rest_framework import serializers
from .models import ExampleModel


class ExmapleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'
