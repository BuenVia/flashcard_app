from django.db import models


class Stage(models.Model):
    stage = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.stage


class GrammarType(models.Model):
    type = models.CharField(max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type


class Word(models.Model):
    eng_word = models.CharField(max_length=55)
    spa_word = models.CharField(max_length=45)
    spa_word_fem = models.CharField(max_length=45, null=True, blank=True)
    grammar_type = models.ForeignKey(GrammarType, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.eng_word
    