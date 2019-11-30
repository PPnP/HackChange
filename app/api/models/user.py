from app.api.models import *


class User(Model):
    id = AutoField()

    class Meta:
        database = db
        db_table = 'Users'
