# Generated by Django 3.2.20 on 2023-08-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DONE', 'DONE'), ('CANCELLED', 'CANCELLED')], default='UNKNOWN', max_length=50),
        ),
    ]
