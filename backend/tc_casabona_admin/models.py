# backend/app_name/models.py

from django.db import models

class SiteConfig(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre du site")
    description = models.TextField(verbose_name="Description")
    contact_email = models.EmailField(verbose_name="Email de contact")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    about = models.TextField(verbose_name="À propos du club")

    def __str__(self):
        return self.title