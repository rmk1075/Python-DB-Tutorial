from models.user import User, Team

class Service():
    def __init__(self):
        pass
    
    def get_users(self):
        users = User.get_all()
        return users
    
    def get_user_by_id(self, id: str=str()):
        user = User.get(id)
        return user
    
    def get_user_by_user_id(self, user_id: str=str()):
        user = User.get_by_user_id(user_id=user_id)
        return user
    
    def create_user(self, user_id: str=str(), name: str=str(), team_id: str=str()):
        user = User.create(user_id=user_id, name=name, team_id=team_id)
        return user
    
    def update_user(self, user_id: str=str(), **kwargs):
        user = self.get_user_by_user_id(user_id=user_id)
        if not user:
            return None
        for k, v in kwargs.items():
            setattr(user, k, v)
        user = User.update(user)
        return user
    
    def get_teams(self):
        teams = Team.get_all()
        return teams
    
    def create_team(self, name: str=str()):
        team = Team.create(name=name)
        return team