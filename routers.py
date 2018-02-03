class BibleViewerRouter(object):
    """
    A router to control all database operations on models in
    the bible_view application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on bible_viewer models to 'nlt2013'
        """
        if model._meta.app_label == 'bible_viewer':
            return 'nlt2013'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on bible_viewer models to 'nlt2013'
        """
        if model._meta.app_label == 'bible_viewer':
            return 'nlt2013'
        return None

    def allow_syncdb(self, db, app_label):

        if db == 'default' and app_label != 'bible_viewer':
            return True
        return None