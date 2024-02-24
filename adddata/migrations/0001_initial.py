# Generated by Django 5.0.2 on 2024-02-20 10:59

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(default=None, max_length=500, null=True, upload_to='brand/')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('carimage', models.ImageField(default=None, max_length=500, null=True, upload_to='cars/')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adddata.brand')),
            ],
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('power', models.IntegerField()),
                ('torque', models.IntegerField()),
                ('to100', models.IntegerField()),
                ('year', models.IntegerField()),
                ('summry', models.TextField()),
                ('infoimage', models.ImageField(default=None, max_length=500, null=True, upload_to='car/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adddata.car')),
            ],
        ),
    ]