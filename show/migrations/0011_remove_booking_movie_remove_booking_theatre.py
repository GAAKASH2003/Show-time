# Generated by Django 4.1.5 on 2023-07-04 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_remove_booking_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='theatre',
        ),
    ]
