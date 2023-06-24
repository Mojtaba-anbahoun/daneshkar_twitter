from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext as _
from core.models import BaseModel
from contents.models import Post, Reaction

# Create your models here.

class User(models.Model):
    full_name = models.CharField(
        max_length=150,
        verbose_name= _("Fullname"),
        blank=False,
        null=False, 
    )
    user_name = models.CharField(
        verbose_name=_("User_Name:"),
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        db_index=True,
        help_text=_("Username to login and show in the profile"),
    )
    password = models.CharField(
        verbose_name=_("Password:"),
        help_text=_("Password to login"),
        max_length=150,
        blank=False,
        null=False,
    )
    image_profile = models.ImageField(
        verbose_name=_("Image:"),
        upload_to="uploads/photos/",
        null=True,
        blank=True,
    )
    bio = models.TextField(_("Biography:"))
    birth_date = models.DateField(_("Birth_date:"), null=True, blank=True,)
    email = models.EmailField(
       verbose_name=_("Email"),
       unique=True,
    )
    join_date = models.DateTimeField(_("Join_date:"))
    age = models.PositiveIntegerField(blank=True, null=True)

    def get_following(self):
        return self.following.all()
    
    def get_followers(self):
        return self.followers.all()
    
    def create_post(self, title, image):
        return Post.objects.create(user=self, title=title, image=image)
    
    def like_post(self, post):
        Reaction.objects.create(user=self, post=post)

    def unlike_post(self, post):
        like = Reaction.objects.filter(user=self, post=post).first()
        if like:
            like.delete()

    @property
    def followers_count(self):
        return self.followers.count()
    
    @property
    def followings_count(self):
        return self.followings.count()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name


class Relation(models.Model):

    from_user = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name="followings")
    to_user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="followers")

    class Meta:
        verbose_name = _("Relation")
        verbose_name_plural = _("Relations")
