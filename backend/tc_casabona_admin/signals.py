
import os
import yaml
import subprocess
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SiteConfig

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

