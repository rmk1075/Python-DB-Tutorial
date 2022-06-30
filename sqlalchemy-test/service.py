from models.user import User

class Service():
    def __init__(self):
        pass
    
    def get_users(self):
        users = User.get()
        return users
    
    def add_user(self, user_id: str=str(), name: str=str()):
        user = User.create(user_id=user_id, name=name)
        return user
    