# Generated by Django 3.0.5 on 2020-05-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_payment_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='room_expiry_date',
            field=models.DateField(null=True),
        ),
    ]