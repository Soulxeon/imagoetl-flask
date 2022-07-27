import psycopg2
from db.config import config

def connect():
    """ Connect to the PostgreSQL database server """

    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    return (conn)

