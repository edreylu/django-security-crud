from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from .models import FormsMenu
from .forms import CreateNewFormsMenu, UpdateFormsMenu
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def formasMenu(request):
    context = {}
    ls = FormsMenu.objects.all()
    context["ls"] = ls
    return render(request, "formas/formas.html",context)


@login_required
def createFormas(request):
    context = {}
    if request.method == "POST":
        form = CreateNewFormsMenu(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El registro fue creado.')
            return HttpResponseRedirect("/formas/")
    else:
        form = CreateNewFormsMenu()
    context["form"] = form
    return render(request, "formas/create.html",context)

@login_required
def updateFormas(request, id):
    context = {}
    if request.method == "POST":
        form = UpdateFormsMenu(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            url = form.cleaned_data["url"]
            icon = form.cleaned_data["icon"]
            FormsMenu.objects.filter(id=id).update(name=name,url=url,icon=icon)
            messages.success(request, 'El registro fue actualizado.')
            return HttpResponseRedirect("/formas/")
    else:
        try:
            forma=FormsMenu.objects.get(id=id)
            form = UpdateFormsMenu(instance=forma)
        except FormsMenu.DoesNotExist:
            raise Http404("Forma does not exist")
    context["form"] = form;
    return render(request, "formas/update.html",context)

@login_required
def deleteFormas(request, id):
    formaExists=FormsMenu.objects.filter(id=id).exists()
    if formaExists:
        FormsMenu.objects.filter(id=id).delete()
    else:
        messages.error(request, 'El registro No fue eliminado.')
        return HttpResponseRedirect("/")
    messages.success(request, 'El registro fue eliminado.')
    return HttpResponseRedirect("/formas/")