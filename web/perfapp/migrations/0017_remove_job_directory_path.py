# Generated by Django 2.1.5 on 2019-04-28 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfapp', '0016_auto_20190428_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='directory_path',
        ),
    ]
