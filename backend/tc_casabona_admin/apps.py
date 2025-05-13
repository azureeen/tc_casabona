from django.apps import AppConfig

class TcCasabonaAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tc_casabona_admin'

    def ready(self):
        # Import des signaux ou d'autres fonctionnalités au démarrage
        import tc_casabona_admin.signals
        pass
