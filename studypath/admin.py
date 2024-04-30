from django.contrib import admin

# Register your models here.
from .models import Word, Stage, GrammarType, Step

admin.site.register(Word)
admin.site.register(Stage)
admin.site.register(GrammarType)
admin.site.register(Step)