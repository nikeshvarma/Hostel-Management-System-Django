from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals
