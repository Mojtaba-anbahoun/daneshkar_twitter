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
    category = models.ForeignKey("Category" , on_delete=models.CASCADE, related_name="categories", default=None)


    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title    
    
    
class Tag(models.Model):
    text = models.CharField(max_length=15)
    posts = models.ManyToManyField(Post , related_name="tags")

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.text


class Image(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30, default=None)
    alt = models.CharField(verbose_name=_("Alternative text"), max_length=30, default=None)
    image = models.FileField(upload_to="uploads/images/")
    is_default = models.BooleanField(_("Is Default"), default=False)
    post = models.ForeignKey(Post , related_name="images", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_to = models.ForeignKey("self", blank=True, null=True , on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user


#class Reaction(BaseModel):
#    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
#    post = models.ForeignKey(Post, on_delete=models.CASCADE)

#    class Meta:
#        verbose_name = _("Reaction")
#        verbose_name_plural = _("Reactions")

#    def __str__(self):
#        return self.user

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        verbose_name=_("Slug"),
        unique=True,
        db_index=True,
    )
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name





