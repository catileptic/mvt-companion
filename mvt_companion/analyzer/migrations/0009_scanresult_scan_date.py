# Generated by Django 4.1 on 2023-07-10 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0008_scanresult_last_security_path_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='scan_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date when the forensic scan was run'),
        ),
    ]