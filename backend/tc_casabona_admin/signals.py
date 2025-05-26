
import os
import yaml
import subprocess
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SiteConfig, BlogPost
from datetime import datetime

@receiver(post_save, sender=SiteConfig)
def update_yaml_and_rebuild_jekyll(sender, instance, **kwargs):
    print(">>>>> Signal déclenché pour SiteConfig")

    # Dictionnaire des données à injecter dans le YML
    data = {
        'title': instance.title,
        'description': instance.description,
    }

    # Chemin du fichier YAML dans le volume partagé
    yaml_path = '/app/_data/site_config.yml'  # Assure-toi que ce chemin correspond au volume monté vers frontend/_data

    os.makedirs(os.path.dirname(yaml_path), exist_ok=True)

    # Écriture du fichier YAML
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

    # Reconstruction automatique du site Jekyll dans le conteneur frontend
    try:
        subprocess.run(
            ["docker", "exec", "tc_casabona_frontend_1", "jekyll", "build"],
            check=True
        )
        print("Build Jekyll terminé avec succès.")
    except subprocess.CalledProcessError as e:
        print("Erreur lors du build Jekyll :", e)
    except FileNotFoundError:
        print("La commande Docker est introuvable. Docker est-il bien installé et lancé ?")




@receiver(post_save, sender=BlogPost)
def create_markdown_post(sender, instance, **kwargs):
    print(">>>>> Signal déclenché pour BlogPost")

    # Chemin du dossier où stocker les posts Markdown (volume monté vers Jekyll)
    markdown_path = '/app/_posts/'  

    # Génération du nom de fichier au format Jekyll : YYYY-MM-DD-title.md
    filename = f"{instance.date.strftime('%Y-%m-%d')}-{instance.title.replace(' ', '-').lower()}.md"
    full_path = os.path.join(markdown_path, filename)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Chemin relatif de l'image pour Jekyll
    if instance.feature_image:
        image_path = f"/media/{instance.feature_image}"
    else:
        image_path = ""  # Si aucune image n'est fournie

    # Contenu du fichier Markdown
    content = f"""---
layout: post
title: "{instance.title}"
description: "{instance.description}"
date: {instance.date}
feature_image: {image_path}
tags: [{', '.join(tag.strip() for tag in instance.tags.split(','))}]
---

{instance.content}
"""

    # Écriture dans le fichier Markdown
    with open(full_path, 'w') as f:
        f.write(content)

    # Reconstruction automatique du site Jekyll dans le conteneur frontend
    try:
        subprocess.run(
            ["docker", "exec", "tc_casabona_frontend_1", "jekyll", "build"],
            check=True
        )
        print("Build Jekyll terminé avec succès.")
    except subprocess.CalledProcessError as e:
        print("Erreur lors du build Jekyll :", e)
    except FileNotFoundError:
        print("La commande Docker est introuvable. Docker est-il bien installé et lancé ?")