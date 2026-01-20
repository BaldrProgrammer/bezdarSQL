import dataclasses

from bsql import update
from bsql.base import Base, Column

@dataclasses.dataclass
class News(Base):
    __tablename__ = 'news'
    id: int = Column(autoincrement=True)
    title: str = Column()
    text: str = Column()
    author_id: int = Column()

    def __todict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text
        }


update(News, values={'author_id': 1, 'title': 'putin dies'}, where={'id': 3})
