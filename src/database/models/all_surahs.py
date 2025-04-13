from src.database.db import metadata, now, default_now
from sqlalchemy import (Column, DateTime, Table, String, Integer)

surahs = Table(
    'surahs',
    metadata,
    Column('number', Integer, primary_key=True),
    Column('name', String),
    Column('english_name', String),
    Column('english_name_translation', String),
    Column('number_of_ayahs', Integer),
    Column('revelation_type', String),
    Column('last_updated', DateTime, nullable=False, onupdate=now,
           **default_now)
)
