from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from .models import Usuario
from .forms import CreateNewUser, UpdateUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def users(request):
    context = {}
    ls = Usuario.objects.all()
    context["ls"] = ls
    return render(request, "usuarios/users.html",context)

@login_required
def usersById(request, id):
    context = {}
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
    return render(request, "usuarios/users.html",context)

@login_required
def createUser(request):
    context = {}
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            u = form.cleaned_data["user"]
            t = Usuario(name=n,last_name=ln,role=r,user=u)
            t.save()
            messages.success(request, 'El registro fue creado.')
            return HttpResponseRedirect("/users/")
    else:
        form = CreateNewUser()
    context["form"] = form
    return render(request, "usuarios/create.html",context)

@login_required
def updateUser(request, id):
    context = {}
    if request.method == "POST":
        form = UpdateUser(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ln = form.cleaned_data["last_name"]
            r = form.cleaned_data["role"]
            u = form.cleaned_data["user"]
            Usuario.objects.filter(id=id).update(name=n,last_name=ln,role=r,user=u)
            messages.success(request, 'El registro fue actualizado.')
            return HttpResponseRedirect("/users/")
    else:
        try:
            usuario=Usuario.objects.get(id=id)
            form = UpdateUser(instance=usuario)
        except Usuario.DoesNotExist:
            raise Http404("User does not exist")
    context["form"] = form;
    return render(request, "usuarios/update.html",context)

@login_required
def deleteUser(request, id):
    usuarioExists=Usuario.objects.filter(id=id).exists()
    if usuarioExists:
        Usuario.objects.filter(id=id).delete()
    else:
        messages.error(request, 'El registro No fue eliminado.')
        return HttpResponseRedirect("/users/")
    messages.success(request, 'El registro fue eliminado.')
    return HttpResponseRedirect("/users/")
