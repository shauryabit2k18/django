# Generated by Django 3.0.5 on 2020-04-06 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Question_text',
            new_name='question_text',
        ),
    ]
