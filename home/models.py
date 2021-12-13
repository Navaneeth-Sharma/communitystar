from django.db import models
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from jsonfield import JSONField

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
    project_urls = JSONField(default=dict)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username

class projectsdetails(models.Model):
    domain = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    title= models.CharField(max_length=200)
    stage=models.CharField(max_length=100)
    prog=models.CharField(max_length=100)
    org=models.CharField(max_length=1)
    count=models.IntegerField()
    framework=models.CharField(max_length=100)
    level=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)

    def __str__(self):
        return self.title

from django.contrib.postgres.fields import ArrayField

    # pieces = 
class projectsTaken(models.Model):
    
    user = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Project Taken'
        verbose_name_plural = 'Projects Taken'

    def __str__(self):
        return self.user