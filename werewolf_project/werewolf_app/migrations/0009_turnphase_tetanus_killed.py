# Generated by Django 2.2 on 2019-12-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf_app', '0008_auto_20191218_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnphase',
            name='tetanus_killed',
            field=models.BooleanField(default=False),
        ),
    ]
