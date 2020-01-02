# Generated by Django 2.0.7 on 2019-12-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opgaver', '0006_kunder_kunde_installation'),
    ]

    operations = [
        migrations.AddField(
            model_name='opgaver',
            name='afsluttet',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kunder',
            name='kontakt_mail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='kunder',
            name='kunde_adresse',
            field=models.TextField(blank=True, help_text='Gadenavn, nr., Postnummer og By', null=True),
        ),
        migrations.AlterField(
            model_name='kunder',
            name='kunde_id',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='kunder',
            name='kunde_installation',
            field=models.TextField(blank=True, null=True),
        ),
    ]