from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import CreateNewUser, UpdateNewUser

# Create your views here.


def index(request):
    return render(request, "main/home.html",{})

def users(request):
    ls = User.objects.all()
    return render(request, "main/users.html",{"ls":ls})

def usersById(request, id):
    ls = User.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("edit"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id))  == "clicked":
                    print("c" + str(item.id))
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(request, "main/users.html",{"ls":ls})

def create(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            t = User(name=n,last_name=ln,role=r)
            t.save()
            request.user.user.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewUser()

    return render(request, "main/create.html",{"form":form})

def update(request, id):
    obj= User.objects.get(id=id)
    if request.method == "POST":
        form = UpdateNewUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            User.objects.filter(id=id).update(name=n,last_name=ln,role=r)
            
        return HttpResponseRedirect("/%i" %id)
    else:
        form = UpdateNewUser(request.POST or None, instance= obj)

    return render(request, "main/update.html",{"form":form})
   