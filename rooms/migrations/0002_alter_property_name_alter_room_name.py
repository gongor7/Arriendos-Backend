# Generated by Django 4.2.4 on 2023-08-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
