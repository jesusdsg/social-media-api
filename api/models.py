from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# custom user
class CustomUser(AbstractUser):
    '''Custom user model with the required fields'''
    # username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    age = models.IntegerField(blank=True)
    phone_number = models.TextField(blank=False)

    # USERNAME_FIELD = email
    REQUIRED_FIELDS = [first_name, phone_number]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# post by users
class Post(models.Model):
    title = models.CharField(max_length=250, blank=False,
                             null=False)
    content = models.CharField(max_length=400, blank=False)
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    ip_adress = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostTag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=100, blank=False)


class PostLike(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
