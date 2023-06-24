from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet
# Create your models here.

class BaseModel(models.Model):

    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)
    class meta:
        abstract = True

class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
    def archives(self):
        return super().get_queryset().filter(is_deleted=True)
    

class SoftDeleteModel(BaseModel):
    objects = MyManager()
    is_deleted = models.BooleanField(default=False, db_index=True)

    def delete(self):
        self.is_deleted = True
        self.save()


    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name
    
class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


