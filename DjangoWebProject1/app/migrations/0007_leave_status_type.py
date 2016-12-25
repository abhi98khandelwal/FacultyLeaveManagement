# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-14 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20161012_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_status',
            name='type',
            field=models.CharField(choices=[('medical', 'Medical Leave'), ('earned', 'Earned Leave'), ('casual', 'Casual Leave'), ('holiday', 'Restricted Holiday Leave'), ('study', 'Study Leave')], default='earned', max_length=7),
        ),
    ]