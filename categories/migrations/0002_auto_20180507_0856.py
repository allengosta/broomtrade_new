# Generated by Django 2.0.5 on 2018-05-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядковый номер'),
        ),
    ]
