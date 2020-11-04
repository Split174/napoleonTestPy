from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class OfferModel(Base):
    """
    The class describes the relationship offers
    """
    __tablename__ = 'offer'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}