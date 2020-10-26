from apps.usuarios.models import Usuario
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

# Create your views here.


def index(request):
    context = {}
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
        formas = usuario.role.formas.all()
        print(formas)
        context["formas"] = formas
    return render(request, "main/home.html",context)

def other(request):
    context = {}

    return render(request,"",context)
