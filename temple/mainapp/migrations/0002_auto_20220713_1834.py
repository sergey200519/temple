# Generated by Django 3.2.6 on 2022-07-13 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='shot_name',
            new_name='shot_title',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name',
            new_name='title',
        ),
    ]
