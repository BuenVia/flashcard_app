from typing import Any
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Word, Stage, GrammarType
from .serializers import WordSerializer, GrammarTypeSerializer


def index(request):
    stages_list = Stage.objects.all()
    return render(request, "studypath/index.html", {"stages": stages_list})


def learn(request, stage):
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


class StudyListCreate(generics.ListCreateAPIView):
    serializer_class = WordSerializer
    
    def get_queryset(self):
        return Word.objects.filter(stage=self.kwargs["stage"])


class GrammarTypeListCreate(generics.ListCreateAPIView):
    
    queryset = GrammarType.objects.all()
    serializer_class = GrammarTypeSerializer

    
