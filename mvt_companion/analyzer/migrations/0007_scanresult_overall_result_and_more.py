# Generated by Django 4.1 on 2023-07-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0006_scanresult_mvt_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='overall_result',
            field=models.CharField(choices=[('warning', 'The scan has produced at lease one warning.'), ('clean', 'The scan is clean! It has produced no warnings, nor detections.')], default='N/A', max_length=100, verbose_name='the overall result of the scan'),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='operating_system',
            field=models.CharField(choices=[('android', 'Android'), ('ios', 'iOS'), ('unknown', 'Unknown OS')], default='unknown', max_length=100, verbose_name='device OS'),
        ),
    ]
