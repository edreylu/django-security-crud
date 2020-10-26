from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from .models import Role
from .forms import CreateNewRole, UpdateRole
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def roles(request):
    context = {}
    ls = Role.objects.all()
    context["ls"] = ls
    return render(request, "roles/roles.html", context)


@login_required
def createRole(request):
    context = {}
    if request.method == "POST":
        form = CreateNewRole(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El registro fue creado.')
            return HttpResponseRedirect("/roles/")
    else:
        form = CreateNewRole()
    context["form"] = form
    return render(request, "roles/create.html", context)


@login_required
def updateRole(request, id):
    context = {}
    if request.method == "POST":
        form = UpdateRole(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            insert = form.cleaned_data["insert"]
            edit = form.cleaned_data["edit"]
            delete = form.cleaned_data["delete"]
            search = form.cleaned_data["search"]
            formas = form.cleaned_data["formas"]
            print(edit)
            reg = Role.objects.get(id=id)
            reg.name=name 
            reg.insert=insert
            reg.edit=edit
            reg.delete=delete
            reg.search=search
            reg.formas.set(formas)
            reg.save()
            messages.success(request, 'El registro fue actualizado.')
            return HttpResponseRedirect("/roles/")
    else:
        try:
            role = Role.objects.get(id=id)
            form = UpdateRole(instance=role)
        except Role.DoesNotExist:
            raise Http404("Role does not exist")
    context["form"] = form;
    return render(request, "roles/update.html", context)


@login_required
def deleteRole(request, id):
    roleExists = Role.objects.filter(id=id).exists()
    if roleExists:
        Role.objects.filter(id=id).delete()
    else:
        messages.error(request, 'El registro No fue eliminado.')
        return HttpResponseRedirect("/roles/")
    messages.success(request, 'El registro fue eliminado.')
    return HttpResponseRedirect("/roles/")

# Create your views here (roles forma).