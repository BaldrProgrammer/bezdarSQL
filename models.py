from bsql import select
from bsql.base import Base, Column

class Ad(Base):
    __tablename__ = 'ads'
    id: int = Column()
    title: str = Column()
    text: str = Column()


selected_ad = select(Ad, value='*', filter_by={'id': '1'})
print()