from models.base import init_db
from service import Service


def run():
    init_db()
    service = Service()
    print(service.get_users())
    print(service.add_user(user_id='test_id', name='test_name'))
    print(service.get_users())
    print(service.add_user(user_id='test_id', name='test_name'))
    print(service.get_users())


if __name__ == '__main__':
    run()