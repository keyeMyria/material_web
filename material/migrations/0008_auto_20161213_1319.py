# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-13 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_auto_20161110_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material', verbose_name='\u5165\u5e93\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='inmaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material', verbose_name='\u51fa\u5e93\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
    ]