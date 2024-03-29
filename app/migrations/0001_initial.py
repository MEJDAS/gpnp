# Generated by Django 5.0.3 on 2024-03-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Responsable Secteur/Service', 'Responsable Secteur/Service'), ('Manufacturing Quality Engineer', 'Manufacturing Quality Engineer'), ('Demandeur', 'Demandeur'), ('FDP Planning Maintenance', 'FDP Planning Maintenance'), ('Receveur', 'Receveur'), ('Responsable Qualité usine', 'Responsable Qualité usine')], max_length=100)),
                ('fullName', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
