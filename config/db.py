from curses import meta
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://gregory:12345@localhost:3306/logincat")

meta_data = MetaData()