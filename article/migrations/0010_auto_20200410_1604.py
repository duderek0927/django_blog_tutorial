# Generated by Django 2.2.7 on 2020-04-10 08:04

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_articlepost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
    ]
