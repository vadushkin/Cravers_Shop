# Generated by Django 4.1.2 on 2022-10-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_remove_ourcompany_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourcompany',
            name='url',
            field=models.URLField(default=1, max_length=100, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
