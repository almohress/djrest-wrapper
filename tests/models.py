from django.db import models
from drfwrapper.interfaces import BaseModel


class ExampleModel(BaseModel):
    text = models.CharField(max_length=10)

    
