from typing import Any
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics
# from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Word, Stage, GrammarType
from .serializers import WordSerializer, GrammarTypeSerializer


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def learn(request, stage):
    grammar_type = GrammarType.objects.filter(stage=stage)
    return render(request, "studypath/learn.html", {
        "stage" : stage, 
        "grammar_type": grammar_type
    })
    
def learn_words(request, stage, gr):
    words = Word.objects.filter(grammar_type=gr)
    return render(request, "studypath/learn-words.html", {"words": words})

def practice(request, stage):
    return render(request, "studypath/practice.html", {"stage": stage})


def test(request, stage):
    return render(request, "studypath/test.html", {"stage": stage})


class WordListCreate(generics.ListCreateAPIView):
    serializer_class = WordSerializer
    
    def get_queryset(self):
        gt = self.request.query_params.get('grammar_type')
        return Word.objects.filter(grammar_type=gt)


class GrammarTypeListCreate(generics.ListCreateAPIView):
    
    queryset = GrammarType.objects.all()
    serializer_class = GrammarTypeSerializer

    
