# backend/app_name/models.py

from django.db import models
from ckeditor.fields import RichTextField

class SiteConfig(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre du site")
    description = models.TextField(verbose_name="Description")
    contact_email = models.EmailField(verbose_name="Email de contact")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    about = models.TextField(verbose_name="À propos du club")

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre de l'article")
    description = models.TextField(verbose_name="Description")
    date = models.DateField(verbose_name="Date de publication")
    feature_image = models.ImageField(upload_to='blog_images/', verbose_name="Image de l'article")
    tags = models.CharField(max_length=255, verbose_name="Tags (séparés par des virgules)")
    content = RichTextField(verbose_name="Contenu de l'article")

    def __str__(self):
        return self.title