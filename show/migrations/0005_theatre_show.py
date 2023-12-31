# Generated by Django 4.1.5 on 2023-07-01 20:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('theatre_id', models.AutoField(primary_key=True, serialize=False)),
                ('theatre_name', models.CharField(max_length=12)),
                ('theatre_address', models.CharField(max_length=15)),
                ('rows', models.PositiveSmallIntegerField(verbose_name=django.core.validators.MaxValueValidator(15))),
                ('cols', models.PositiveSmallIntegerField(verbose_name=django.core.validators.MaxValueValidator(15))),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('time', models.CharField(choices=[('Morning Show', '10:30-12:00'), ('Evening Show', '1:00-3:30'), ('Second Show', '5:00-6:30')], max_length=25)),
                ('price', models.IntegerField(default=250)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.movie')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.theatre')),
            ],
        ),
    ]
