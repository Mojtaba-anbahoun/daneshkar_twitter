from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.utils.translation import gettext as _
from core.models import BaseModel, TimeStampMixin

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
    password = models.IntegerField(
        verbose_name=_("Password:"),
        help_text=_("Password to login"),
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

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name


class Relation(TimeStampMixin):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")
    to_user = models.ForeignKey(User , on_delete=models.CASCADE, related_name="followers")

    class Meta:
        verbose_name = _("Relation")
        verbose_name_plural = _("Relations")

    def __str__(self):
        return self.from_user
