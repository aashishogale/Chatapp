# Generated by Django 2.0.1 on 2018-01-23 10:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('last_activity_ip', models.GenericIPAddressField()),
                ('last_activity_date', models.DateTimeField(default=datetime.datetime(1950, 1, 1, 0, 0))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
