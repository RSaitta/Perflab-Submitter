# Generated by Django 2.1.5 on 2019-04-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfapp', '0012_auto_20190424_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
    ]
