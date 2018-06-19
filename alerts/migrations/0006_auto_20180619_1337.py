# Generated by Django 2.0.6 on 2018-06-19 13:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_auto_20180617_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='frequency',
            field=models.IntegerField(choices=[(2, 'Every 2 minutes'), (10, 'Every 10 minutes'), (30, 'Every 30 minutes')], default=10),
        ),
        migrations.AlterField(
            model_name='alert',
            name='search_terms',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message="Search can't be empty", regex='\\S')]),
        ),
    ]
