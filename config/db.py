import logging

from decouple import config
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists


class DataBaseHandler():

    def __init__(self):
        self.default_database=config("DB_DEFAULT_NAME")        
        self.ams=config("DB_AMS")
        self.user=config("DB_USER")
        self.password=config("DB_PASSWORD")
        self.host=config("DB_HOST")
        self.port= config("DB_PORT")
        self.orm= config("ORM_NAME")
        self.driver = config("ORM_DRIVER")
        self.base_url = f"{self.orm}+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/"

    def create_db(self, db_name : str):
        url = self.base_url+db_name
        try:
            if not database_exists(url):
                create_database(url)
                print("The database has been created.")
            else:
                print("The database already exists.")
            return url
            
        except Exception as e :
            session.rollback()
            print(e)

# logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
# logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)
handler= DataBaseHandler()
engine = create_engine(handler.create_db(config("DB_AMS")),pool_pre_ping=True)
meta = MetaData(engine)
conn = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


