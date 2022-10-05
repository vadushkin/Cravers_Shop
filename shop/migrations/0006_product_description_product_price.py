# Generated by Django 4.1.1 on 2022-10-04 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, max_length=300, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(limit_value=10000000, message='Максимум 10000000$')], verbose_name='Цена'),
        ),
    ]