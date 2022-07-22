from models.user import User

class Service():
    def __init__(self):
        pass
    
    def get_users(self):
        users = User.get_all()
        return users
    
    def get_user_by_id(self, id: str=str()):
        user = User.get(id)
        return user
    
    def add_user(self, user_id: str=str(), name: str=str()):
        user = User.create(user_id=user_id, name=name)
        return user
    