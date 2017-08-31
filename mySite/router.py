class App01Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == 'app01':
            return 'test01'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'app01':
            return 'test01'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'app01' or \
           obj2._meta.app_label == 'app01':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'app01':
            return db == 'test01'
        return None


import random

class App02Router(object):
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        # return random.choice(['test01', 'test02'])
        if model._meta.app_label == 'app02':
            return 'test02'
        return None

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        if model._meta.app_label == 'app02':
            return 'test02'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_list = ('test02')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        if app_label == 'app02':
            return True
        return None