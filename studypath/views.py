from django.shortcuts import render, HttpResponse

from .models import Stage

# Create your views here.
def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def stages(request, stage):
    return HttpResponse("You are looking at stage %s" % stage)