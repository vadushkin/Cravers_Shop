# Generated by Django 4.1.2 on 2022-10-08 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_popularcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularcategory',
            name='level',
        ),
        migrations.RemoveField(
            model_name='popularcategory',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='popularcategory',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='popularcategory',
            name='tree_id',
        ),
    ]
