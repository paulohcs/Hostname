# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=15)),
                ('mac_address', models.CharField(max_length=17)),
                ('ip_address', models.TextField(unique=True)),
            ],
        ),
    ]