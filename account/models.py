from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name=_("User"))
    phone_number = models.CharField(max_length=11,verbose_name=_("Phone Number"))
    image = models.ImageField(
        upload_to="images/profiles",
        null=True,
        blank=True,
        verbose_name=_("Image")
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
