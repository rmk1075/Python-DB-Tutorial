from models.base import init_db
from service import Service


def run():
    init_db()
    service = Service()
    
    team1 = service.create_team(name="team1")
    print(f"new team. team1={team1}")
    
    user1 = service.create_user(user_id="user1", name="one", team_id=team1.id)
    print(f"new user. user1={user1}")
    user2 = service.create_user(user_id="user2", name="two", team_id=team1.id)
    print(f"new user. user2={user2}")
    
    print("--------------------------------------------------")
    
    team2 = service.create_team(name="team2")
    print(f"new team. team2={team2}")
    user = service.update_user(user_id="user2", team_id=team2.id)
    print(f"update user. user={user}")
    
    print("--------------------------------------------------")
    
    print("print out users of each team")
    print(team1.users)
    print(team2.users)
    
    
if __name__ == '__main__':
    run()