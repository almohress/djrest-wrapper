from rest_framework.serializers import ModelSerializer
from .models import ExampleModel


class ExmapleReqSerializer(ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'
        execlude = ['id']


class ExampleResSerializer(ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = '__all__'
