# Generated by Django 4.1 on 2023-07-09 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0007_scanresult_overall_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='last_security_path_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date of the last security scan'),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='overall_result',
            field=models.CharField(choices=[('warning', 'The scan has produced at least one warning.'), ('clean', 'The scan is clean! It has produced no warnings, nor detections.')], default='N/A', max_length=100, verbose_name='the overall result of the scan'),
        ),
    ]
