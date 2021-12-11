from django.db import models
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User

# Create your models here.

class UserSocialAuth(UserSocialAuth):
    name = models.CharField(max_length=200) 
    class Meta:
        verbose_name = 'User Social Auth'
        verbose_name_plural = 'User Social Auths'

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    project_urls = models.JSONField(default=dict)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username