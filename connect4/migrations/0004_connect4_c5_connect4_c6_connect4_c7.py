# Generated by Django 4.1.4 on 2022-12-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0003_connect4_z7'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect4',
            name='c5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='connect4',
            name='c6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='connect4',
            name='c7',
            field=models.IntegerField(default=0),
        ),
    ]
