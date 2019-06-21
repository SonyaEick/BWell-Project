# Generated by Django 2.2.2 on 2019-06-21 19:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mortality', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='city',
            field=models.CharField(default=datetime.datetime(2019, 6, 21, 19, 50, 8, 97937, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cause',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
