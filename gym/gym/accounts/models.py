from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from gym.accounts.managers import GymUserManager


class GymUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'

    objects = GymUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )
    last_name = models.CharField(
        max_length=25,
    )
    user = models.OneToOneField(
        GymUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
