from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(models.Model):
    # Define user roles
    ROLE_CHOICES = (
        ('Responsable Secteur/Service', 'Responsable Secteur/Service'),
        ('Manufacturing Quality Engineer', 'Manufacturing Quality Engineer'),
        ('Demandeur', 'Demandeur'),
        ('FDP Planning Maintenance', 'FDP Planning Maintenance'),
        ('Receveur', 'Receveur'),
        ('Responsable Qualité usine', 'Responsable Qualité usine'),
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    # Additional fields as needed
    # For example, you can add fields for name, date of signature, etc.
    fullName = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
