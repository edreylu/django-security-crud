from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Usuario
from .forms import CreateNewUser, UpdateUser
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22

# Create your views here.


def index(request):
    return render(request, "main/home.html",{})

@login_required
def users(request):
<<<<<<< HEAD
    context = {}
    ls = Usuario.objects.all()
    context["ls"] = ls
    return render(request, "main/users/users.html",context)
=======
    ls = Usuario.objects.all()
    return render(request, "main/users.html",{"ls":ls})
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22

@login_required
def usersById(request, id):
<<<<<<< HEAD
    context = {}
=======
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22
    ls = Usuario.objects.get(id=id)
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
    context["ls"] = ls
    return render(request, "main/users/users.html",context)

@login_required
def create(request):
    context = {}
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            t = Usuario(name=n,last_name=ln,role=r)
            t.save()
            return HttpResponseRedirect("/users/")
    else:
        form = CreateNewUser()
    context["form"] = form
    return render(request, "main/users/create.html",context)

@login_required
def update(request, id):
<<<<<<< HEAD
    context = {}
=======
    
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22
    if request.method == "POST":
        form = UpdateUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            Usuario.objects.filter(id=id).update(name=n,last_name=ln,role=r)
<<<<<<< HEAD
            return HttpResponseRedirect("/users/")
=======
            
        return HttpResponseRedirect("/%i" %id)
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22
    else:
        try:
            usuario=Usuario.objects.get(id=id)
            form = UpdateUser(instance=usuario)
        except Usuario.DoesNotExist:
            raise Http404("User does not exist")
<<<<<<< HEAD
    context["form"] = form;
    return render(request, "main/users/update.html",context)
=======
>>>>>>> 626311025f64afb4f177ebb1fc9a7df42744de22

@login_required
def delete(request, id):
    usuarioExists=Usuario.objects.filter(id=id).exists()
    if usuarioExists:
        Usuario.objects.filter(id=id).delete()
    else:
        return HttpResponseRedirect("/users/1")
    
    return HttpResponseRedirect("/users/")