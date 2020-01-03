from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Opgaver, Kunder
from django.views.generic import (CreateView, UpdateView, DeleteView, ListView)

from .forms import OpgaverForm, KunderForm


def home_view(request, *args, **kwargs):
    return render(request, "home.html")


def opgaver_opret_view(request, *args, **kwargs):
    obj = Opgaver.objects.get(id=1)
    form = OpgaverForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OpgaverForm()
        return redirect('/opgaver')

    context = {'form': form}
    return render(request, "opgaver/opgaver_opret.html", context)


def opgaver_detail_view(request):
    queryset = Opgaver.objects.all()  # Liste med alle opgave objecter
    context = {"object_list": queryset}
    return render(request, "opgaver/opgaver_detail.html", context)


def opgaver_slet_view(request, id):
    obj = get_object_or_404(Opgaver, id=id)
    # POST request
    if request.method == "POST":
        # Godkend sletning
        obj.delete()
        return redirect('/opgaver')
    context = {"object": obj}

    return render(request, "opgaver/opgaver_slet.html", context)


def kunder_opret_view(request, *args, **kwargs):
    obj = Kunder.objects.get(id=1)
    form = KunderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = KunderForm()
        return redirect('/kunder')

    context = {'form': form}
    return render(request, "kunder/kunder_opret.html", context)


def kunder_detail_view(request, *args, **kwargs):
    queryset = Kunder.objects.all()  # Liste med alle opgave objecter
    context = {"object_list": queryset}
    return render(request, "kunder/kunder_detail.html", context)
