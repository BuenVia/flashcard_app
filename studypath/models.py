from django.db import models


class Stage(models.Model):
    stage = models.IntegerField()
    name = models.CharField(max_length=90)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.name


class GrammarType(models.Model):
    type = models.CharField(max_length=45)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.type
    
    class Meta:
        managed = True
        db_table = 'studypath_grammartype'

class Step(models.Model):
    step = models.IntegerField()
    description = models.CharField(max_length=45)
    grammar_type = models.ForeignKey(GrammarType, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.name
    
    class Meta:
        managed = True
        db_table = 'studypath_step'

class Word(models.Model):
    eng_word = models.CharField(max_length=55)
    fre_word = models.CharField(max_length=45)
    fre_word_fem = models.CharField(max_length=45, null=True, blank=True)
    grammar_type = models.ForeignKey(GrammarType, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.eng_word
    
    class Meta:
        managed = True
        db_table = 'studypath_word'
        