from django.apps import AppConfig

date_dict = {}


class BibleViewerConfig(AppConfig):
    name = 'bible_viewer'

    def ready(self):
        from bible_viewer.plan_builder import plan
        global date_dict
        date_dict = plan()
