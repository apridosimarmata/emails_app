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

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email_address = Column(String(255))

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class EventRegistration(Base):
    __tablename__ = 'event_registration'
    
    people_id = Column(Integer, primary_key=True)
    event_id = Column(String(255))

