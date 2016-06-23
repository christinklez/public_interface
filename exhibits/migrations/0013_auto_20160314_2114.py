# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0012_theme_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkText', models.CharField(max_length=200)),
                ('linkLocation', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BrowseTermGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupTitle', models.CharField(max_length=200)),
                ('order', positions.fields.PositionField(default=-1)),
                ('browseTerms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibits.BrowseTerm')),
            ],
        ),
        migrations.AddField(
            model_name='theme',
            name='browseTermGroupsOrder',
            field=positions.fields.PositionField(default=-1),
        ),
        migrations.AddField(
            model_name='theme',
            name='browseTerms',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='exhibits.BrowseTermGroups'),
            preserve_default=False,
        ),
    ]