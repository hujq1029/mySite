# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, null=True, blank=True)),
            ],
            options={
                'db_table': 'hobby',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64, null=True, blank=True)),
                ('password', models.CharField(max_length=64, null=True, blank=True)),
                ('hobby', models.ForeignKey(blank=True, to='app02.Hobby', null=True)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
