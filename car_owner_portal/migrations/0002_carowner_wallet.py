# Generated by Django 2.0.3 on 2018-04-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_owner_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carowner',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]
