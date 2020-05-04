# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-27 17:40
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


def adiciona_token_de_usuarios(apps, schema_editor):
    for user in get_user_model().objects.all():
        Token.objects.get_or_create(user=user)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(adiciona_token_de_usuarios)
    ]
