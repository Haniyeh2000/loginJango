# Generated by Django 3.2.5 on 2021-08-03 13:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210803_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 13, 17, 26, 92265, tzinfo=utc)),
        ),
    ]
