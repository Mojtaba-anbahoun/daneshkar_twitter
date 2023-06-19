from django.db import models
from uuid import uuid4

# Create your models here.

class BaseModel(models.Model):
    class meta:
        abstract = True

    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)


class TimeStampMixin:
    class meta:
        abstract = True
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


