# Generated by Django 4.1.3 on 2023-09-03 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0001_initial'),
        ('emplois_temps', '0007_seance_cour_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seance_cour',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.filiere'),
        ),
    ]
