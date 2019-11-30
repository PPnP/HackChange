from app.api.models import *


class Locker(Model):
    id = AutoField()

    class Meta:
        database = db
        db_table = 'Lockers'
