from django.db import models
from drf_wrapper.interfaces import BaseModel


class ExampleModel(BaseModel):
    text = models.CharField(max_length=10)

    
