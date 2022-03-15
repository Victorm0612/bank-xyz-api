# Generated by Django 4.0.2 on 2022-03-15 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_alter_ticket_ordernumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='serviceId',
        ),
        migrations.AddField(
            model_name='ticket',
            name='serviceId',
            field=models.ManyToManyField(to='Core.Service'),
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='userId',
        ),
        migrations.AddField(
            model_name='ticket',
            name='userId',
            field=models.ManyToManyField(to='Core.User'),
        ),
    ]
