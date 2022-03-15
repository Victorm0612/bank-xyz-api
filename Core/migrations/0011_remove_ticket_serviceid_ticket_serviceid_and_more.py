# Generated by Django 4.0.2 on 2022-03-15 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0010_remove_ticket_serviceid_ticket_serviceid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='serviceId',
        ),
        migrations.AddField(
            model_name='ticket',
            name='serviceId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.service'),
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='userId',
        ),
        migrations.AddField(
            model_name='ticket',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.user'),
        ),
    ]
