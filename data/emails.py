from app import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Emails(Base):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, primary_key=True)
    email_subject = db.Column(db.String)
    email_content = db.Column(db.String)
    timestamp = db.Column(db.Timestamp)

class People(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email_address = db.Column(db.String)

class Event(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class EventRegistration(Base):
    people_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.String)

'''
CREATE TABLE people (
    id serial PRIMARY KEY,
    name VARCHAR(255),
    email_address VARCHAR(255)
);

CREATE TABLE event (
    id serial PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE event_registration (
    people_id INTEGER PRIMARY KEY,
    event_id INTEGER,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (event_id) REFERENCES event (id)
);

INSERT INTO people (name, email_address) VALUES ('Rudi', 'rudi@example.com');
INSERT INTO people (name, email_address) VALUES ('Andi', 'andi@example.com');
INSERT INTO people (name, email_address) VALUES ('Siti', 'siti@example.com');

INSERT INTO event (name) VALUES ('Seminar Web Development');
INSERT INTO event (name) VALUES ('Workshop Mobile Development');

INSERT INTO event_registration (people_id, event_id) VALUES (1, 1);
INSERT INTO event_registration (people_id, event_id) VALUES (2, 2);
INSERT INTO event_registration (people_id, event_id) VALUES (3, 1);

'''