# Generated by Django 2.2 on 2020-01-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_stranger', '0002_auto_20200118_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
