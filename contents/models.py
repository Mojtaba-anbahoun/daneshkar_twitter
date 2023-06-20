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


    def is_liked_by_user(self, user) -> bool:
        return self.reaction_set.filter(user=user).exists()

    def add_like(self, user):
        return Reaction.objects.create(user=user, post=self)
    
    def remove_like(self, user):
        like = Reaction.objects.get(user=user, post=self)
        return like

    def add_comment(self, user, text):
        return Comment.objects.create(user=user, post=self, text=text)
    
    def get_comments(self):
        return Comment.objects.filter(post=self)
    
    def delete_comments(self):
        Comment.objects.filter(post=self).delete()

    def get_likes_count(self):
        return Reaction.objects.filter(post=self).count()
    
    def get_comments_count(self):
        return Comment.objects.filter(post=self).count()
    

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

    def get_replies(self):
        return Comment.objects.filter(reply_to=self)

    def edit_comment(self, new_text):
        self.text = new_text
        self.save()
    
    def delete_comment(self):
        self.delete()

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.user


class Reaction(BaseModel, TimeStampMixin):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    post_field = models.ForeignKey(Post, verbose_name= _("Post"), on_delete=models.CASCADE)

    def unlike(self):
        self.delete()

    class Meta:
        verbose_name = _("Reaction")
        verbose_name_plural = _("Reactions")

    def __str__(self):
        return self.user

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





