from django.shortcuts import render, HttpResponse, redirect
from .models import UserSocialAuth, UserProfile
from django.http import request 
from django.contrib.auth import authenticate
from django.contrib import auth
import requests 

def get_data(username):
    res = requests.get('https://api.github.com/users/'+str(username)).json()
    print(username)
    return res['avatar_url'], res['name']

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # fetch all the data from the database for the user
        return redirect('/dashboard')
    return render(request, 'index.html', {'listofprojects': UserProfile.objects.all()})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # print(request.user)
    for i in range(len(UserProfile.objects.all())):
        if UserProfile.objects.all()[i].user == request.user:
            return render(request, 'dashboard.html', {'listofprojects': UserProfile.objects.all()[0].project_urls})
    
    img, name =  get_data(request.user)
    UserProfile.objects.create(user=request.user, name=name, image=img)

    return render(request, 'dashboard.html')

def create(request):
    return render(request, 'createpage.html')


# <!-- <button>Sign in</button>
#                         <p style="margin-right: -300px;"><a href="{{url_for('forgotpassword')}}" style=" color: #d4dce1;;">Forgot
#                                 password?</a></p>
                                
#                             <h5>
#                         <h5>
#                             <span style="color: #d4dce1;">Don't have an account?</span>
#                             <b> <a href="{{url_for('signup')}}" style="color: #ec4141" class="pointer">Sign up</a></b>

#                         </h5> -->

#                         <!-- {% with messages = get_flashed_messages() %}
#                         {% if messages %}
#                                 {% for message in messages %}
#                                 <div class="alert alert-warning alert-dismissible" style="color: green;">
                                
#                                           {{ message }}
#                                         </div>
#                                 {% endfor %}
#                         {% endif %}
#                     {% endwith %} -->