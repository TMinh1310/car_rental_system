# Generated by Django 4.0.3 on 2024-01-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_owner_portal', '0003_alter_carowner_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carowner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]