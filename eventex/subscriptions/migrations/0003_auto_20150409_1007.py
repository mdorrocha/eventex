# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscription_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email', blank=True),
        ),
    ]
