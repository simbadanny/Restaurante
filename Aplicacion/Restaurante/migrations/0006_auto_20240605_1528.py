# Generated by Django 3.0.7 on 2024-06-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0005_auto_20240605_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesas',
            name='numero_mes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]