from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import Word, Stage


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def learn(request, stage):
    words_list = Word.objects.filter(stage=stage)
    testlist = Word.objects.filter(stage=stage).values('grammar_type').annotate(dcount=Count('grammar_type'))

    noun_article_list = words_list.filter(grammar_type=1)
    pronoun_list = words_list.filter(grammar_type=2)
    adjectives_list = words_list.filter(grammar_type=3)

    
    
    return render(request, "studypath/learn.html", {
        "stage" : stage, 
        "words": words_list, 
        "articles": noun_article_list,
        "pronouns": pronoun_list,
        "adjectives": adjectives_list,
        "testlist": tes
        })


def practice(request, stage):
    return render(request, "studypath/practice.html", {"stage": stage})


def test(request, stage):
    return render(request, "studypath/test.html", {"stage": stage})
