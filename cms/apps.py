from django.apps import AppConfig


class CmsConfig(AppConfig):
    name = 'cms'

    def ready(self):
       """
       This function is called when startup.
       """
       from .update import start # <= さっき作った start関数をインポート
       start()
