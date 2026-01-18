from bsql import select
from bsql.base import Base, Column

class Ad(Base):
    __tablename__ = 'ads'
    id: int = Column()
    title: str = Column()
    text: str = Column()

    def __todict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text
        }


selected_ad = select(Ad, value='*', filter_by={'id': '1'})
print(selected_ad.__todict__())