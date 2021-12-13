from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserSocialAuth)
admin.site.register(UserProfile)
admin.site.register(projectsdetails)
admin.site.register(projectsTaken)