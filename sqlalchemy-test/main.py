from models.base import init_db
from service import Service


def run():
    init_db()
    service = Service()
    print(f"service.get_users()::{service.get_users()}")
    print(f"service.add_user(user_id='test_id', name='test_name')::{service.add_user(user_id='test_id', name='test_name')}")
    print(f"service.get_users()::{service.get_users()}")
    # print(f"service.add_user(user_id='test_id', name='test_name')::{service.add_user(user_id='test_id', name='test_name')}")
    # print(f"service.get_user()::{service.get_users()}")
    
    for i in range(10):
        user = service.add_user(user_id=str(i), name=f"user{i}")
        print(f"added user: {user}")

    print(f"service.get_users()::{service.get_users()}")


if __name__ == '__main__':
    run()