# Generated by Django 3.2.5 on 2021-07-17 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bookingform_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
