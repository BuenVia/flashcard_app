from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("learn/<int:stage>", views.learn, name="learn"),
    path("learn-data/<int:stage>", views.StudyListCreate.as_view(), name="studydata"),
    path("learn-data1/<int:stage>", views.GrammarTypeListCreate.as_view(), name="grammartype"),
    path("practice/<int:stage>", views.practice, name="practice"),
    path("test/<int:stage>", views.test, name="test")
]
