# Generated by Django 4.0.2 on 2022-03-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_location_ticket_updatetime_ticket_locationid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
