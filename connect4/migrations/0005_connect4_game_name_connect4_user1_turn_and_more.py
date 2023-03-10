# Generated by Django 4.1.4 on 2022-12-29 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0004_connect4_c5_connect4_c6_connect4_c7'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect4',
            name='game_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connect4',
            name='user1_turn',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='connect4',
            name='user2_turn',
            field=models.BooleanField(default=False),
        ),
    ]
