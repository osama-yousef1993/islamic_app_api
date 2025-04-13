from src.database.db import metadata, now, default_now
from sqlalchemy import (JSON, Column, DateTime, Integer, Table, String)

surahs_details = Table(
    'surahs_details',
    metadata,
    Column('surah_number', Integer, primary_key=True),
    Column('surah_name', String),
    Column('surah_english_name', String),
    Column('surah_english_name_translation', String),
    Column('surah_revelation_type', String),
    Column('surah_ayahs_ar', JSON),
    Column('surah_ayahs_en', JSON),
    Column('last_updated', DateTime, nullable=False, onupdate=now,
           **default_now)
)
