from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("studypath/", include("studypath.urls")),
    path("flashcards/", include("cards.urls")),
]
