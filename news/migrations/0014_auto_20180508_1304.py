# Generated by Django 2.0.5 on 2018-05-08 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20180508_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 8, 13, 4, 57, 435301), verbose_name='Опубликована'),
        ),
    ]
