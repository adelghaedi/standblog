from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="کاربر")
    phone_number = models.CharField(max_length=11,verbose_name="شماره تلفن")
    image = models.ImageField(
        upload_to="images/profiles",
        null=True,
        blank=True,
        verbose_name="تصویر"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب های کاربری"
