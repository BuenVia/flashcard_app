from django.shortcuts import render, HttpResponse

from .models import Word, Stage, GrammarType


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def stages(request, stage):
    words_list = Word.objects.filter(stage=stage)
    noun_article_list = words_list.filter(grammar_type=1)
    pronoun_list = words_list.filter(grammar_type=2)
    adjectives_list = words_list.filter(grammar_type=3)
    return render(request, "studypath/stage.html", {
        "stage" : stage, 
        "words": words_list, 
        "articles": noun_article_list,
        "pronouns": pronoun_list,
        "adjectives": adjectives_list
        })
