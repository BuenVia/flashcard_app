from django.contrib import admin

# Register your models here.
from .models import Word, Stage, GrammarType

admin.site.register(Word)
admin.site.register(Stage)
admin.site.register(GrammarType)