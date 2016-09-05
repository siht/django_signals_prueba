from django.apps import AppConfig

class App2Config(AppConfig):
    name = 'app2'

    def ready(self):
        import app2.signals

