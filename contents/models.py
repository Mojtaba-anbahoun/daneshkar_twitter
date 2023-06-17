from django.db import models
from core.models import BaseModel, TimeStampMixin
from django.utils.translation import gettext as _
# Create your models here.


class Post(TimeStampMixin, BaseModel):
    title = models.CharField(
        verbose_name=_("Title:"),
        max_length=200,
    )
    body = models.TextField(_("Body:"))
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name = "posts",
    )
    image_url = models.ImageField(
        verbose_name= _("Image:"),
        upload_to="images_file",
        null=True,
        blank=True,
    )
    
class Tag(models.Model):
    text = models.CharField(max_length=15)
    posts = models.ManyToManyField(Post , related_name="tags")


class Image(models.Model):
    image = models.FileField(upload_to="uploads/images/")
    post = models.ForeignKey(Post , related_name="images", on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey("accounts.User")
    post = models.ForeignKey(Post)
    reply_to = models.ForeignKey("self", blank=True, null=True)


class Reaction(BaseModel):
    user = models.ForeignKey("accounta.User")
    post = models.ForeignKey(Post)


    






