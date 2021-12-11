from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def dashboard(request):
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