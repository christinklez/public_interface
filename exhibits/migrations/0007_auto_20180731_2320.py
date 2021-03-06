# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-31 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0006_auto_20180731_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalessay',
            name='copyright_holder',
            field=models.TextField(default='Regents of the University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalessay',
            name='copyright_year',
            field=models.IntegerField(default='2011'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalessay',
            name='curator',
            field=models.TextField(default='University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='copyright_holder',
            field=models.TextField(default='Regents of the University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='copyright_year',
            field=models.IntegerField(default='2011'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonplan',
            name='curator',
            field=models.TextField(default='University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='copyright_holder',
            field=models.TextField(default='Regents of the University of California'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='copyright_year',
            field=models.IntegerField(default='2011'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='curator',
            field=models.TextField(default='University of California'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='byline',
            field=models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits'),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='byline_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as'),
        ),
        migrations.AlterField(
            model_name='historicalessay',
            name='byline',
            field=models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits'),
        ),
        migrations.AlterField(
            model_name='historicalessay',
            name='byline_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as'),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='byline',
            field=models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits'),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='byline_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='byline',
            field=models.TextField(blank=True, help_text='Curator name(s) and titles, Any other collaborators, Institutional affiliation, Date of publication', verbose_name='Credits'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='byline_render_as',
            field=models.CharField(choices=[('H', 'HTML'), ('T', 'Plain Text'), ('M', 'Markdown')], default='H', max_length=1, verbose_name='Render credits as'),
        ),
    ]
