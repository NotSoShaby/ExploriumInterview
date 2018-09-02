from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TreeSum(Base):
    __tablename__ = 'tree_sum_table'

    id = Column(Integer, primary_key=True)
    sum = Column(Integer)
    date_inserted = Column(DateTime)

    def __repr__(self):
        return "<TreeSum(id='%s', sum='%s', date inserted='%s')>" % (
                             self.id, self.sum, self.date_inserted)