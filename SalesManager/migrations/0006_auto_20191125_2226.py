# Generated by Django 2.2.7 on 2019-11-25 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SalesManager', '0005_auto_20191125_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=6), max_digits=6),
        ),
        migrations.AlterField(
            model_name='storage',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 19, 26, 4, 688348, tzinfo=utc), verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='last_edition',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 19, 26, 4, 688348, tzinfo=utc), verbose_name='edition date'),
        ),
        migrations.AlterField(
            model_name='storageaction',
            name='action_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 19, 26, 6, 329769, tzinfo=utc), verbose_name='real date'),
        ),
        migrations.AlterField(
            model_name='storageaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 19, 26, 6, 329769, tzinfo=utc), verbose_name='creation date'),
        ),
    ]