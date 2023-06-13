from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Users(models.Model):
    full_name = models.CharField(_("Nama:"), max_length=150)
    user_name = models.CharField(_("User_Name:"), max_length=150)
    password = models.IntegerField(_("Password:"), max_length=30)
    bio = models.TextField(_("Biography:"))
    image_profile = models.ImageField(_("Image:"), upload_to="images_file",
                                      null=True, blank=True)
    birth_date = models.DateField(_("Birth_date:"), null=True, blank=True)
    email = models.EmailField(_("Email:"), 
                              verbose_name="email address",
                              max_length=255,
                              unique=True,)
    join_date = models.DateTimeField(_("Join_date:"))

class Post(models.Model):
    caption = models.CharField(_("Caption:"), max_length=100)
    body = models.TextField(_("Body:"))
    create_at = models.DateField(_("Create_at"))
    image_url = models.ImageField(_("Image:"), upload_to="images_file",
                                      null=True, blank=True)
    