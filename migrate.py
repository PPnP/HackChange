from app.api.models.user import User


User.drop_table()
User.create_table()
