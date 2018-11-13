from config.group_filter_config import group_filter_config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine(group_filter_config['db_url'])
Base = declarative_base()

from models import *
sess = sessionmaker(bind=engine)
