# Generated by Django 4.1.3 on 2023-08-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emplois_temps', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cour',
            name='niveau',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.niveau'),
        ),
    ]