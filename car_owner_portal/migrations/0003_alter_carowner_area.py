# Generated by Django 4.0.3 on 2024-01-14 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_owner_portal', '0002_carowner_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carowner',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_owner_portal.area'),
        ),
    ]
