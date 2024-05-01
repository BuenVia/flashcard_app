from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("learn/<int:stage>", views.learn, name="learn"),
    path("learn/<int:stage>/vocab/<int:gr>", views.learn_words, name="learn-words"),

    path("learn-data", views.WordListCreate.as_view(), name="words"),
    
    path("practice/<int:stage>", views.practice, name="practice"),
    path("test/<int:stage>", views.test, name="test")
]
