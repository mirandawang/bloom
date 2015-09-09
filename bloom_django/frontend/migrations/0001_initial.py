# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'backgrounds/')),
                ('promo_image', models.ImageField(upload_to=b'promo_images/')),
            ],
        ),
        migrations.CreateModel(
            name='PlantImageZipFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_base', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=b'plant_zips/')),
            ],
        ),
        migrations.CreateModel(
            name='PlantType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sample_image', models.ImageField(upload_to=b'plant_type_samples/')),
                ('piece_image', models.ImageField(upload_to=b'plant_type_pieces/')),
                ('imagezip', models.OneToOneField(to='frontend.PlantImageZipFile')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='frontend.Player', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'pots/')),
            ],
        ),
        migrations.CreateModel(
            name='PressDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('press_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plant_name', models.CharField(max_length=100, null=True)),
                ('press_date', models.ManyToManyField(to='frontend.PressDate')),
            ],
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_press', models.DateField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('day_num', models.IntegerField(default=0)),
                ('background', models.ForeignKey(to='frontend.Background')),
                ('owner', models.ForeignKey(to='frontend.Player')),
                ('pot', models.ForeignKey(to='frontend.Pot')),
                ('timeline', models.OneToOneField(to='frontend.Timeline')),
                ('type', models.ForeignKey(to='frontend.PlantType')),
            ],
        ),
    ]
