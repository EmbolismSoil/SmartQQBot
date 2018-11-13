from . import Base, engine
from datetime import datetime
from sqlalchemy import Column, Integer, String, BLOB, DateTime, TIMESTAMP, Text

class Massage(Base):
    __tablename__ = 'group_message'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    sender_name = Column(String(128), index=True, nullable=False)
    sender_id = Column(String(128), index=True, nullable=True)
    group_name = Column(String(128), index=True, nullable=True)
    group_id = Column(String(128), index=True, nullable=True)
    when = Column(DateTime, index=True, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
