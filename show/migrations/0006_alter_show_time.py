# Generated by Django 4.1.5 on 2023-07-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0005_theatre_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='time',
            field=models.TimeField(default='10.30'),
        ),
    ]
