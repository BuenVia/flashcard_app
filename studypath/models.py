from django.db import models

# Create your models here.
class Word(models.Model):
    eng_word = models.CharField(max_length=45)
    spa_word = models.CharField(max_length=45)
    grammar_type = models.CharField(max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.spa_word
    
class Stage(models.Model):
    stage = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)