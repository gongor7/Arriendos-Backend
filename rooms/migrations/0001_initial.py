# Generated by Django 4.2.4 on 2023-11-29 12:41

from django.db import migrations, models
import django.db.models.deletion
import rooms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(upload_to=rooms.models.Property.get_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('capacity', models.IntegerField()),
                ('warranty', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('group', models.CharField(max_length=100)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.property')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField(null=True)),
                ('state', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
        ),
    ]
