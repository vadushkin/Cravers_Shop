# Generated by Django 4.1.1 on 2022-10-03 15:32

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_category_parent_menucategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.menucategory', verbose_name='Родительская категория'),
        ),
    ]