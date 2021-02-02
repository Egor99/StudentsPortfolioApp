# Generated by Django 3.1.5 on 2021-01-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('results', models.CharField(max_length=512)),
                ('rating', models.FloatField()),
                ('university', models.CharField(max_length=128)),
                ('speciality', models.CharField(max_length=256)),
                ('graduate', models.BooleanField(default=False)),
            ],
        ),
    ]
