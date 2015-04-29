# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z0-9-_ ]+$', b'Only numbers, letters, underscores, dashes and spaces are allowed.')])),
                ('index_url', models.URLField()),
                ('image', models.TextField(max_length=256, null=True, blank=True)),
                ('build', models.TextField(max_length=265, null=True, blank=True)),
                ('command', models.TextField(max_length=256)),
                ('expose_publicly', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.TextField(max_length=64, null=True, blank=True)),
                ('external', models.BooleanField(default=False)),
                ('from_app', models.ForeignKey(related_name='links', to='base.App')),
                ('to_app', models.ForeignKey(to='base.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('internal_port', models.IntegerField()),
                ('service_name', models.TextField(max_length=64, null=True, blank=True)),
                ('app', models.ForeignKey(related_name='ports', to='base.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('high_port', models.IntegerField(null=True, blank=True)),
                ('public_path_base', models.TextField(null=True, blank=True)),
                ('running', models.BooleanField(default=False)),
                ('app', models.ForeignKey(to='base.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContainerPort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('external_port', models.IntegerField()),
                ('app_port', models.ForeignKey(to='base.AppPort')),
                ('container', models.ForeignKey(related_name='mapped_ports', to='base.Container')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnvVar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=64)),
                ('value', models.TextField(default=b'', max_length=256)),
                ('app', models.ForeignKey(related_name='environment_variables', to='base.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z0-9-_ ]+$', b'Only numbers, letters, underscores, dashes and spaces are allowed.')])),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(blank=True)),
                ('uploaded_data', models.FileField(default=None, validators=[django.core.validators.RegexValidator(b'.*\\.(ZIP|zip)$', b'Only compressed archive (.zip) files are allowed.')], upload_to=b'', blank=True, null=True)),
                ('data_folder', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VolumeMount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mounted_at', models.TextField(max_length=254)),
                ('located_at', models.TextField(max_length=254)),
                ('read_only', models.BooleanField(default=False)),
                ('app', models.ForeignKey(to='base.App')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='container',
            name='project',
            field=models.ForeignKey(to='base.Project'),
            preserve_default=True,
        ),
    ]