from app.api.models.user import Locker


Locker.drop_table()
Locker.create_table()
