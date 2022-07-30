import psycopg2
from db_imago.config import config

def connect():
    """ Connect to the PostgreSQL database server """

    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
    cur.execute('SELECT * FROM test;')
    testdata = cur.fetchall()
    cur.close()
    conn.close()

    return (testdata)

