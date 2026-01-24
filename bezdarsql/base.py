import dataclasses


class Column:
    def __init__(self, **kwargs):
        self.autoincrement = kwargs.get('autoincrement')


    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name


@dataclasses.dataclass
class Base:
    __tablename__ = None
