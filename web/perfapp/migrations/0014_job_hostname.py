# Generated by Django 2.1.5 on 2019-04-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfapp', '0013_auto_20190424_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='hostname',
            field=models.CharField(default='', max_length=100),
        ),
    ]