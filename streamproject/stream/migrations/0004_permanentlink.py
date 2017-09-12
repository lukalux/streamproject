# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0003_link_reallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermanentLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateTimeField()),
                ('realLink', models.CharField(blank=True, max_length=2000)),
                ('created_at', models.DateField(auto_now=True)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['modified_at'],
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
