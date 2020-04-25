# Generated by Django 2.2 on 2019-12-18 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('werewolf_app', '0004_role_hastetanus'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winning_players',
            field=models.ManyToManyField(related_name='games_won', to='login_app.User'),
        ),
    ]
