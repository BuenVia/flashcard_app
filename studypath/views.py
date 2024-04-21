from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import Word, Stage, GrammarType


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def learn(request, stage):
    # words_list = Word.objects.filter(stage=stage)
    # noun_article_list = words_list.filter(grammar_type=1)
    # pronoun_list = words_list.filter(grammar_type=2)
    # adjectives_list = words_list.filter(grammar_type=3)
    
    study_list = []
    grammar_type = GrammarType.objects.all()

    for gt in grammar_type:
        words = Word.objects.filter(stage=stage).filter(grammar_type=gt)
        word_list = { 'grammar_type': gt.type, "words": words }
        study_list.append(word_list)

    return render(request, "studypath/learn.html", {
        "stage" : stage, 
        "study_list": study_list
        })


def practice(request, stage):
    return render(request, "studypath/practice.html", {"stage": stage})


def test(request, stage):
    return render(request, "studypath/test.html", {"stage": stage})
