from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.utils.translation import gettext as _

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
        vebose_name=_("Password:"),
        max_length=128,
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


