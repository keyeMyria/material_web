# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 15:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0005_auto_20161031_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmaterial',
            name='count',
            field=models.IntegerField(default=0, verbose_name='\u5165\u5e93\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='inmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ins', to='material.Material', verbose_name='\u5165\u5e93\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='inmaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ins', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='\u51fa\u5e93\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outs', to='material.Material', verbose_name='\u51fa\u5e93\u6750\u6599'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='usage',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u9886\u6599\u7528\u9014'),
        ),
        migrations.AlterField(
            model_name='outmaterial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='outs', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
