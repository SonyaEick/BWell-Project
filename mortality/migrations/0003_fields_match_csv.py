# Generated by Django 2.2.2 on 2019-06-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortality', '0002_added_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='city',
        ),
        migrations.AddField(
            model_name='cause',
            name='cancer',
            field=models.CharField(default='-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='county_code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='county_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='hiv',
            field=models.CharField(default='-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='homicide',
            field=models.CharField(default='-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='injury',
            field=models.CharField(default='-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='state_code',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='state_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='strata_id',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='suicide',
            field=models.CharField(default='-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='cause',
            name='time_span',
            field=models.CharField(default='-1111', max_length=255),
        ),
    ]
