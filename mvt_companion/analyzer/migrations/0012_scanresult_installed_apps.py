# Generated by Django 4.1 on 2023-07-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0011_alter_scanresult_warnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='installed_apps',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]