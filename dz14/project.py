import json

from exc import *
from user import User


class Project:
    PATH = 'users.json'

    @classmethod
    def get_users_list(cls, file_name='users.json'):
        with open(file_name, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
            return cls(users_list)

    def login(self, other):
        for user in self.users_list:
            if user == other:
                other.level = user.level
                self.admin = other
                break
        else:
            raise AccesError(other.name, other.uid)

    def add_user(self, other):
        if other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_list.append(other)

    def remove_user(self, other):
        if other not in self.users_list:
            raise AccesError(other.name, other.uid)
        elif other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_list.remove(other)

    def __init__(self, users_list=None):
        self.users_list = users_list or []
        self.admin = None

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.PATH, 'w', encoding='utf-8') as f:
            my_dict = {}
            for user in self.users_list:
                if user.level not in my_dict:
                    my_dict[user.level] = {}
                my_dict[user.level][user.uid] = user.name
            json.dump(my_dict, f)

    def __str__(self):
        return f'Project {self.__dict__}'

    def __enter__(self):
        return self


u1 = User('Ben', 1, 1)
with Project.get_users_list() as p:
    p.login(u1)
