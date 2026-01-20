import dataclasses

from bsql import delete
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


delete(News, where={'id': 3, 'author_id': 2})
