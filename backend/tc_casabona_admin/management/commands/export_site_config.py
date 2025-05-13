
import yaml
from django.core.management.base import BaseCommand
from tc_casabona_admin.models import SiteConfig

class Command(BaseCommand):
    help = 'Exporte la configuration du site vers un fichier YAML lisible par Jekyll'

    def handle(self, *args, **options):
        config = SiteConfig.objects.last()

        if not config:
            self.stdout.write(self.style.ERROR("Aucune configuration trouvée."))
            return

        data = {
            'title': config.title,
            'description': config.description,
            'contact_email': config.contact_email,
            # ajoute ici les champs de ton modèle
        }

        with open('/app/_data/site_config.yml', 'w') as f:
            yaml.dump(data, f, allow_unicode=True)

        self.stdout.write(self.style.SUCCESS("Configuration exportée vers _data/site_config.yml"))
