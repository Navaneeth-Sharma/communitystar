import requests
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import UserProfile, projectsdetails, projectsTaken


def get_data(username):
    res = requests.get("https://api.github.com/users/" + str(username)).json()
    print(username)
    return res["avatar_url"], res["name"]


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        # fetch all the data from the database for the user
        return redirect("/dashboard")
    return render(request, "index.html", {"listofprojects": UserProfile.objects.all()})


def login(request):
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("/")


@csrf_exempt
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        try:
            projectsTaken.objects.create(
                user=request.user,
                project=request.POST["title"],
                url=request.POST["url"],
            )
        except Exception as e:
            print(e)
            pass

    for i in range(len(UserProfile.objects.all())):
        if UserProfile.objects.all()[i].user == request.user:

            return render(
                request,
                "dashboard.html",
                {
                    "listofprojects": projectsTaken.objects.filter(user=request.user)
                    .only("project", "url")
                    .values_list("project", "url")
                    .distinct(),
                    "allproject": projectsdetails.objects.all(),
                    "avatar_url": get_data(request.user)[0],
                },
            )

    img, name = get_data(request.user)
    UserProfile.objects.create(user=request.user, name=name, image=img)
    return render(request, "dashboard.html")


@csrf_exempt
def create(request):
    if request.method == "POST":
        print("msk")
        projectsdetails.objects.create(
            domain=request.POST["domain"],
            os=request.POST["OS"],
            link=request.POST["Link"],
            creator=request.user,
            description=request.POST["description"],
            title=request.POST["title"],
            stage=request.POST["stage"],
            prog=request.POST["prog"],
            org=request.POST["org"],
            count=request.POST["count"],
            framework=request.POST["framework"],
            level=request.POST["level"],
        )
        return redirect("/dashboard")

    return render(request, "createpage.html")
