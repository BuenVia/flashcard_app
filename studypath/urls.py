from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("learn/<int:stage>", views.learn, name="learn"),
    path("practice/<int:stage>", views.practice, name="practice"),
    path("test/<int:stage>", views.test, name="practice")
]
