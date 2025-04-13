from dotenv.main import load_dotenv
from os import getenv


load_dotenv()

DATE_FORMAT = '%Y/%m/%d'

#
#
#
# ------------- General App setting ----------
#
#
#
APP_NAME = getenv("APP_NAME", "Islamic App sync job")
APP_VERSION = getenv("APP_VERSION", "0.1.0")

#
#
#
# ------------- Database Connection ----------
#
#
#
DB_DATABASE = getenv('DB_DATABASE')
DB_USERNAME = getenv('DB_USERNAME')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')


def get_sqlalchemy_database_url():
    """
    Generate sqlalchemy database url from env vars.
    """
    return 'postgresql://{}:{}@{}:{}/{}'.format(
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_DATABASE
    )
