from bezdarsql import select, select_join
import dataclasses
from bezdarsql.base import Base, Column


@dataclasses.dataclass
class User(Base):
    __tablename__ = 'users'

    id: int = Column(autoincrement=True)
    name: str = Column()
    username: str = Column()
    password: str = Column()
    role: str = Column()
    ulga: int = Column()
    tickets: str = Column()


@dataclasses.dataclass()
class Relief(Base):
    __tablename__ = 'reliefs'

    id: int = Column(autoincrement=True)
    title: str = Column()
    description: str = Column()
    discount: int = Column()


print(select_join((User, Relief), value='*', filter_by=({User.id: '14'})))
