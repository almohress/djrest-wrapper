from django.db import models
from djrest_wrapper.interfaces import BaseModel


class ExampleModel(BaseModel):
    text = models.CharField(max_length=10)
    some_unique_field = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'example'
        verbose_name_plural = 'examples'
