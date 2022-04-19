# Generated by Django 4.0.4 on 2022-04-13 07:36

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_problem_prob_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='prob_link',
            field=models.FilePathField(path=pathlib.PureWindowsPath('C:/Users/91917/new-django-project/gs24/Files')),
        ),
        migrations.AlterField(
            model_name='problem',
            name='test_input',
            field=models.FilePathField(path=pathlib.PureWindowsPath('C:/Users/91917/new-django-project/gs24/TEST-INPUT')),
        ),
        migrations.AlterField(
            model_name='problem',
            name='test_output',
            field=models.FilePathField(path=pathlib.PureWindowsPath('C:/Users/91917/new-django-project/gs24/TEST-OUTPUT')),
        ),
    ]