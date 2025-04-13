from src.database.db import metadata, now, default_now
from sqlalchemy import (Column, DateTime, Table, String, ARRAY, JSON)

readers = Table(
    'readers',
    metadata,
    Column('identifier', String, primary_key=True),
    Column('language', String),
    Column('name', String),
    Column('arabic_name', String),
    Column('english_name', String),
    Column('format', String),
    Column('type', String),
    Column('surahs', JSON),
    Column('last_updated', DateTime, nullable=False, onupdate=now,
           **default_now)
)

all_readers = Table(
    'all_readers',
    metadata,
    Column('identifier', String, primary_key=True),
    Column('language', String),
    Column('name', String),
    Column('arabic_name', String),
    Column('english_name', String),
    Column('format', String),
    Column('type', String),
    Column('surahs_sounds', ARRAY(String)),
    Column('last_updated', DateTime, nullable=False, onupdate=now,
           **default_now)
)
