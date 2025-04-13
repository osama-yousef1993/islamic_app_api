from datetime import datetime

from sqlalchemy import create_engine, MetaData, func

from src.utils.config import get_sqlalchemy_database_url


engine = create_engine(get_sqlalchemy_database_url())

metadata = MetaData()
metadata.bind = engine
now = datetime.now()
default_now = dict(default=now, server_default=func.now())
