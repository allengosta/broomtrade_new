# Generated by Django 2.0.5 on 2018-05-07 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180507_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 7, 13, 23, 57, 431560), verbose_name='Опубликована'),
        ),
    ]
