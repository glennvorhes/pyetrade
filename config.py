from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from sqlalchemy.orm.session import Session

import os

__author__ = 'glenn'

sandbox = True

# etrade login
user_name = os.environ['ETRADE_USER']
user_pwd = os.environ['ETRADE_PWD']

if sandbox:
    oauth_consumer_key = os.environ['ETRADE_CONSUMER_KEY_SANDBOX']
    consumer_secret = os.environ['ETRADE_CONSUMER_SECRET_SANDBOX']
else:
    oauth_consumer_key = os.environ['ETRADE_CONSUMER_KEY']
    consumer_secret = os.environ['ETRADE_CONSUMER_SECRET']

# min quote count to use for evaluation
min_quote_count = 300

null_flag = -999.99


engine = None

# use pyscopg to check connection
_port = 5432
_usr = 'postgres'

psyco_template = 'port={port} dbname={db} host={host} user={usr} password={pwd}'
sqla_tmpl = 'postgresql://{usr}:{pwd}@{host}:{port}/{db}'

use_local = True

if use_local:
    pass
    # conn = psycopg2.connect(psyco_template.format(usr=_usr, pwd=_pwd, host=_host, port=_port, db=_db))
    # conn.close()
    # engine = create_engine(sqla_tmpl.format(usr=_usr, pwd=_pwd, host=_host, port=_port, db=_db))

else:
    pass
    # conn = psycopg2.connect(psyco_template.format(usr=_usr, pwd=_pwd, host=_host, port=_port, db=_db))
    # conn.close()
    # engine = create_engine(sqla_tmpl.format(usr=_usr, pwd=_pwd, host=_host, port=_port, db=_db))

_Session = scoped_session(sessionmaker(bind=engine))

#
# def open_sqlalchemy_session():
#     """
#
#     :return:
#     :rtype: Session
#     """
#     return _Session()

Base = declarative_base(bind=engine)
