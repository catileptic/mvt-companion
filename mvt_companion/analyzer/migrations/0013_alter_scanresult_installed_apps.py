# Generated by Django 4.1 on 2023-07-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0012_scanresult_installed_apps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanresult',
            name='installed_apps',
            field=models.JSONField(blank=True),
        ),
    ]
