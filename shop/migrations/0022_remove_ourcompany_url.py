# Generated by Django 4.1.2 on 2022-10-08 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_ourcompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourcompany',
            name='url',
        ),
    ]
