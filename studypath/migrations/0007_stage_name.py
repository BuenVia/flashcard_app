# Generated by Django 4.0.4 on 2024-04-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studypath', '0006_alter_grammartype_options_alter_word_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='name',
            field=models.CharField(default='tbc', max_length=90),
            preserve_default=False,
        ),
    ]