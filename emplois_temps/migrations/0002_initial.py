# Generated by Django 4.1.3 on 2023-08-26 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departement', '0001_initial'),
        ('utilisateurs', '0001_initial'),
        ('emplois_temps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance_td',
            name='enseignant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.enseignant'),
        ),
        migrations.AddField(
            model_name='seance_td',
            name='filiere',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departement.filiere'),
        ),
        migrations.AddField(
            model_name='seance_td',
            name='group_td',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.group_td'),
        ),
        migrations.AddField(
            model_name='seance_td',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.niveau'),
        ),
        migrations.AddField(
            model_name='seance_td',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.salle'),
        ),
        migrations.AddField(
            model_name='seance_cour',
            name='cour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.cour'),
        ),
        migrations.AddField(
            model_name='seance_cour',
            name='enseignant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateurs.enseignant'),
        ),
        migrations.AddField(
            model_name='seance_cour',
            name='filiere',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departement.filiere'),
        ),
        migrations.AddField(
            model_name='seance_cour',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.niveau'),
        ),
        migrations.AddField(
            model_name='seance_cour',
            name='salle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplois_temps.salle'),
        ),
        migrations.AddField(
            model_name='salle',
            name='departement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departement.departement'),
        ),
        migrations.AddField(
            model_name='niveau',
            name='filiere',
            field=models.ManyToManyField(to='departement.filiere'),
        ),
        migrations.AddField(
            model_name='group_td',
            name='niveau',
            field=models.ManyToManyField(to='emplois_temps.niveau'),
        ),
        migrations.AlterUniqueTogether(
            name='seance_td',
            unique_together={('enseignant', 'date_debut', 'date_fin')},
        ),
        migrations.AlterUniqueTogether(
            name='seance_cour',
            unique_together={('enseignant', 'date_debut', 'date_fin')},
        ),
    ]
