from django.shortcuts import render
from django.http import HttpResponse
from .models import Viand


def index(request):

    viands = Viand.objects.all()

    context = {"viands": viands}

    return render(request, "index.html", context)
