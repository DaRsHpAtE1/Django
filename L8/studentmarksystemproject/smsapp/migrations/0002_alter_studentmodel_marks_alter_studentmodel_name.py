# Generated by Django 4.1.1 on 2023-02-23 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='marks',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
