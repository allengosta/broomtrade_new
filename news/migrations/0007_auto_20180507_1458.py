# Generated by Django 2.0.5 on 2018-05-07 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20180507_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 7, 14, 58, 4, 648835), verbose_name='Опубликована'),
        ),
    ]
