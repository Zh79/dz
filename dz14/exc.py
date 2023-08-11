class BasicException(Exception):
    pass


class LevelError(BasicException):
    def __init__(self, us_lvl, ad_lvl):
        self.us_lvl = us_lvl
        self.ad_lvl = ad_lvl

    def __str__(self):
        return f"Уровень {self.ad_lvl} ниже {self.us_lvl}"


class AccesError(BasicException):
    def __init__(self, u_name, u_id):
        self.u_name = u_name
        self.u_id = u_id

    def __str__(self):
        return f'Нет такого пользователя'
