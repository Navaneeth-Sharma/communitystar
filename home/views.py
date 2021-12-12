from django.shortcuts import render, HttpResponse, redirect
from .models import UserSocialAuth, UserProfile, projectsTaken, projectsdetails
from django.http import request 
from django.contrib.auth import authenticate
from django.contrib import auth
import requests 
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

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

def logout(request):
    auth_logout(request)
    return redirect('/')

@csrf_exempt
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    # print(request.user)
    # for i in projectsdetails.objects.all():
    #     print(i)
    if request.method == 'POST':
        if len(projectsTaken.objects.all()) != 0:
            print("hajjakanjwn")
            for i in projectsTaken.objects.all():
                if i.user == request.user:
                    i.project = request.POST.get("title")
                    i.save()
        else:
            print("hajjakanjwn")
            projectsTaken.objects.create(user=request.user, project = request.POST["title"])
    
    for i in range(len(UserProfile.objects.all())):
        if UserProfile.objects.all()[i].user == request.user:
            return render(request, 'dashboard.html', {'listofprojects': UserProfile.objects.all()[0].project_urls['0'],
            'allproject': projectsdetails.objects.all()})
            
    
    img, name =  get_data(request.user)
    UserProfile.objects.create(user=request.user, name=name, image=img)

    return render(request, 'dashboard.html')




@csrf_exempt
def create(request):
    if request.method == 'POST':
        print("msk")
        projectsdetails.objects.create(domain=request.POST['domain'],
                                        os=request.POST['OS'],
                                        link=request.POST['Link'],
                                        creator=request.user,
                                        description=request.POST['description'],
                                        title=request.POST['title'],
                                        stage=request.POST['stage'],prog=request.POST['prog'],
                                        org=request.POST['org'],count=request.POST['count'],
                                        framework=request.POST['framework'],level=request.POST['level'])
        print("NSJJK")
        return redirect('/dashboard')
       
    return render(request, 'createpage.html')




# <div id="content" class="pmd-content content-area dashboard">
# 		<div class="container page-container">
# 			<div class="row gutters">
# 				{% for project in allproject %}
# 				<form method="POST" action="">
# 					<div class="col-xl-3 col-lg-3 col-md-3 col-sm-4 col-12">
# 						<figure class="user-card green">
# 							<figcaption>
# 								<img src="../static/assets/img/favicon.png" alt="Soeng Souy" class="profile">
# 								<h5><a name="title" href={{project.link}}>{{project.title}}</a></h5>
# 								<h6 name="user">@{{project.creator}}</h6>
# 								<p>{{project.description}}</p>

# 								<div class="clearfix">
# 									<span class="badge badge-pill badge-info">{{project.prog}}</span>
# 									<span class="badge badge-pill badge-error">{{project.framework}}</span>
# 									<span class="badge badge-pill badge-success">{{project.org}}</span>
# 								</div>
# 							</figcaption>
# 						</figure>
# 						<button class="buttons" type="submit"> I'm in </button>
# 					</div>
# 				</form>
# 				{% endfor %}
# 			</div>
# 		</div>
# 	</div>

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