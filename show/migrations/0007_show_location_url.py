# Generated by Django 4.1.5 on 2023-07-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0006_alter_show_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='location_url',
            field=models.CharField(default='https://maps.google.co.in/?q=17.437147,78.448591(AAA%20Cinemas:%20Ameerpet)', max_length=100),
        ),
    ]
