# Generated by Django 2.2.26 on 2022-03-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0003_auto_20220311_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamer',
            name='rating',
            field=models.FloatField(default=0, max_length=3),
        ),
    ]
