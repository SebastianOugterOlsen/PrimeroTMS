from django.http import HttpResponse
from django.shortcuts import render
from .models import Opgaver
# Create your views here.
from .forms import OpgaverForm

def opgaver_create_view(request):
    obj = Opgaver.objects.get()
    form = OpgaverForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OpgaverForm()

    context = {
        'form': form
    }
    return render(request,"opgaver/opgaver_create.html", context)


def opgaver_detail_view(request):
    obj = Opgaver.objects.all()
    context = {'object': obj}
    return render(request,"opgaver/opgaver_detail.html", context)