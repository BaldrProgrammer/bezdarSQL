import dataclasses

from bsql import select, insert
from bsql.base import Base, Column

from typing import Optional

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
my_news = News(title='europe overtakes us army', text='european army budget rised to 3 trillion euro, what is 5% from their gdp - 61trillion. leader is germany with 500 billion.', author_id=1)

insert(my_news)
