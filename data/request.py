from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Emails(Base):
    __tablename__ = 'emails'
    
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    email_subject = Column(String(255))
    email_content = Column(Text)
    timestamp = Column(DateTime)
