# Generated by Django 4.1 on 2023-06-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=215, verbose_name='name of the backup')),
                ('date_added', models.DateTimeField(verbose_name='date and time when a backup was added to the database')),
            ],
        ),
    ]
