# Generated by Django 2.1.7 on 2019-05-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfapp', '0030_auto_20190504_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='max_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
