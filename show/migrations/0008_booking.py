# Generated by Django 4.1.5 on 2023-07-02 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0007_show_location_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('row_no', models.SmallIntegerField(unique=True)),
                ('col_no', models.SmallIntegerField(unique=True)),
                ('status', models.IntegerField(choices=[('1', 'Available'), ('2', 'Booked')], default=1)),
                ('session', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.movie')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.show', unique=True)),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.theatre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]