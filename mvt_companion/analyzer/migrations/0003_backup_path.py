# Generated by Django 4.1 on 2023-06-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_rename_phone_backup'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup',
            name='path',
            field=models.CharField(default='', max_length=1000, verbose_name='backup directory file system path'),
            preserve_default=False,
        ),
    ]
