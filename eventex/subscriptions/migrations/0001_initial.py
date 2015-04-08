# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(unique=True, max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=20, verbose_name='telefone', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name': 'inscri\xe7\xe3o',
                'verbose_name_plural': 'inscri\xe7\xf5es',
            },
        ),
    ]
