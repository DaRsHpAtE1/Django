# Generated by Django 4.1.1 on 2023-02-24 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeptModel',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StuModel',
            fields=[
                ('rno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.deptmodel')),
            ],
        ),
    ]
