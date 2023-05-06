import sqlalchemy

from config.db import Base, engine


def create_db_tables():
    user_exist=sqlalchemy.inspect(engine).has_table("users")
    if user_exist == False:
        print("= user Table doesn't exist=")
        Base.metadata.tables["users"].create(engine)
        print("= user Table was created=")
    else:
        print("= user Table exists=")
   