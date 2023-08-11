class User:
    def __init__(self, name, user_id, level=None):
        self.name = name
        self.uid = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.uid == other.uid

    def __repr__(self):
        return f'User {self.name=}, {self.uid=}, {self.level= }'

    def __str__(self):
        return f'User {self.name} with id <{self.u_id}>, level <{self.level}>'
