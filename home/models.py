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



# <!DOCTYPE html>
# <html lang="en">

# <head>
#   <meta charset="UTF-8" />
#   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#   <title>Community Star</title>
#   <link href="https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css" rel="stylesheet" />

#   <link href="https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css" rel="stylesheet" />
#   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css" />
#   <link rel="stylesheet" href="../static/assets/css/questionstyle.css" />
#   <link href="../static/assets/img/favicon.png" rel="icon">
#   <link href="../static/assets/img/favicon.png" rel=" apple-touch-icon">

# </head>

# <body>
#   {% csrf_token %}
#   <div id="container" class="container">
#     <!-- form section -->
#     <div class="row">
#       <h1 style="color:#d4dce1; font-family:Mulish;margin-left: 30%;">Please answer to the questions below!</h1>
#       {% csrf_token %}
#       <form name="test" method="POST" action="/create">
#         {% csrf_token %}
#         <div class="question">
#           <p>Select the relevant operating systems</p>
#           <select name="OS" required>
#             <option value="Windows">Windows </option>
#             <option value="MacOs">MacOS</option>
#             <option value="iOS">iOS</option>
#             <option value="Android">Android</option>
#             <option value="Linux">Linux</option>
#           </select>
#         </div>

#         <div class="question">
#           <p>Select the domain of the project</p>
#           <select name="domain" required>
#             <option value="AI/ML">AI/ML</option>
#             <option value="WEB DEV">Web Development</option>
#             <option value="MOBILE APP">Mobile App</option>
#             <option value="IOT">IOT</option>
#           </select>
#         </div>
#         <div class="question">
#           <p>Please provide project title</p>
#           <input style="width: 30%;" type="text" name="title" id="title" required>
#         </div>
#         <div class="question">
#           <p>Please provide the Link of the repository</p>
#           <input style="width: 30%;" type="url" name="Link" id="Link" required>
#         </div>
#         <div class="question">
#           <p>Select the stage of development the project is in.?</p>
#           <textarea style="width: 30%;" name="stage" required></textarea>
#         </div>
#         <div class="question">
#           <p>Which programming language are you using?</p>
#           <textarea style="width: 30%;" name="prog" required></textarea>
#         </div>
#         <div class="question">
#           <p>Are you from an organization</p>
#           <select name="org" required>
#             <option value="1">Yes </option>
#             <option value="0">No</option>
#           </select>

#         </div>
#         <div class="question">
#           <p>If yes how many people are working on the project?</p>
#           <textarea style="width: 30%;" name="count" required></textarea>
#         </div>
#         <div class="question">
#           <p>Which framework are you using?</p>
#           <textarea style="width: 30%;" name="framework" required></textarea>
#         </div>
#         <div class="question">
#           <p>Description</p>
#           <textarea style="width: 30%; heigth=150%" name="description" required></textarea>
#         </div>
#         <div class="question">
#           <p>Rate the level of the project</p>
#           <select name="level" required>
#             <option value="Windows">Beginner </option>
#             <option value="MacOs">Expert</option>
#             <option value="iOS">Pro</option>

#           </select>
#         </div>
#         <button type="submit" class="buttons" value="Submit">Submit</button>
#       </form>



#     </div>

#   </div>

# </body>
# <!-- <script src="./index.js"></script> -->

# </html>