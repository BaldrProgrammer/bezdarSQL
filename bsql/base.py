import dataclasses


class Column:
    pass

@dataclasses.dataclass
class Base:
    __tablename__ = None