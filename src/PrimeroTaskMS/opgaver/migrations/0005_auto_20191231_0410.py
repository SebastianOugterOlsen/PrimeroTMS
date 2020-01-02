# Generated by Django 2.0.7 on 2019-12-31 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgaver', '0004_auto_20191215_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kunder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kunde_id', models.CharField(max_length=4)),
                ('kunde_navn', models.CharField(max_length=30)),
                ('kunde_adresse', models.TextField()),
                ('kontaktperson', models.CharField(max_length=30)),
                ('kontakt_tlf', models.CharField(max_length=10)),
                ('kontakt_mail', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='opgaver',
            name='deadline',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='opgaver',
            name='kunde_navn',
            field=models.CharField(max_length=30),
        ),
    ]