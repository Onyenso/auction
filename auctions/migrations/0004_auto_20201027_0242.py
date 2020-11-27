# Generated by Django 3.1.2 on 2020-10-27 02:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201027_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])]),
        ),
    ]