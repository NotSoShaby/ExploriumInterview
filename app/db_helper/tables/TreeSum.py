from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TreeSum(Base):
    """ A class that defines the DB table. Inherit from declarative_base() and follows SQLalchemy format """

    __tablename__ = 'tree_sum_table'

    id = Column(Integer, primary_key=True)
    nodes_sum = Column(Integer)
    date_inserted = Column(DateTime)

    def __repr__(self):
        return "<TreeSum(nodes_sum='%s', date inserted='%s')>" % (
                             self.nodes_sum, self.date_inserted)