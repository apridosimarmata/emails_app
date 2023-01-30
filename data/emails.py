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
CREATE TABLE orang (
    id serial PRIMARY KEY,
    nama VARCHAR(255),
    alamat_email VARCHAR(255)
);

CREATE TABLE acara (
    id serial PRIMARY KEY,
    nama VARCHAR(255)
);

CREATE TABLE pendaftaran_acara (
    id_orang INTEGER PRIMARY KEY,
    id_acara INTEGER,
    FOREIGN KEY (id_orang) REFERENCES orang (id),
    FOREIGN KEY (id_acara) REFERENCES acara (id)
);
INSERT INTO orang (nama, alamat_email) VALUES ('Rudi', 'rudi@example.com');
INSERT INTO orang (nama, alamat_email) VALUES ('Andi', 'andi@example.com');
INSERT INTO orang (nama, alamat_email) VALUES ('Siti', 'siti@example.com');

INSERT INTO acara (nama) VALUES ('Seminar Web Development');
INSERT INTO acara (nama) VALUES ('Workshop Mobile Development');

INSERT INTO pendaftaran_acara (id_orang, id_acara) VALUES (1, 1);
INSERT INTO pendaftaran_acara (id_orang, id_acara) VALUES (2, 2);
INSERT INTO pendaftaran_acara (id_orang, id_acara) VALUES (3, 1);

'''