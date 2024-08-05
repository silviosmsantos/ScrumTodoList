# Generated by Django 4.2.3 on 2024-08-05 22:31

import core.validators.permission_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=255, validators=[core.validators.permission_validators.validate_permission_name]),
        ),
    ]