from django.shortcuts import render, HttpResponse

from .models import Word, Stage


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def stages(request, stage):
    words_list = Word.objects.all()
    return render(request, "studypath/stage.html", {"stage" : stage, "words": words_list})
