# Generated by Django 2.2 on 2019-12-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf_app', '0010_auto_20191218_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnphase',
            name='elder_voted_off',
            field=models.BooleanField(default=False),
        ),
    ]
