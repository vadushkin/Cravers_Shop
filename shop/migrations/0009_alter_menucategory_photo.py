# Generated by Django 4.1.1 on 2022-10-03 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_menucategory_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='categories/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['img', 'svg', 'png', 'jpeg', 'ico', 'webp'], message='Этот формат фотографии не подходит')], verbose_name='Фотография'),
        ),
    ]