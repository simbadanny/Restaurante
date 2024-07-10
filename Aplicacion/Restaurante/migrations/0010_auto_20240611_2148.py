# Generated by Django 3.0.7 on 2024-06-12 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0009_auto_20240609_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='promociones',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Restaurante.Menus'),
        ),
        migrations.DeleteModel(
            name='Promociones_Menus',
        ),
    ]