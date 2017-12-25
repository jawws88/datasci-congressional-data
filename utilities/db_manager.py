"""Creating a class that will manage interactions with Postgres Database"""
import urllib.parse

import pandas as pd
import psycopg2 as ps
import sqlalchemy as sa

from utilities.util_functions import df_to_sql


class DBManager(object):

    def __init__(self, db_url):
        self.db_url = db_url
        result = urllib.parse.urlparse(db_url)
        self.host = result.hostname
        self.user = result.username
        self.dbname = result.path[1:]
        self.password = result.password
        self.engine = sa.create_engine(db_url)

    def create_schema(self, schema):
        """Creates schema if does not exist"""
        conn_string = "host={0} user={1} dbname={2} password={3}".format(
            self.host, self.user, self.dbname, self.password)
        conn = ps.connect(conn_string)
        with conn:
            cur = conn.cursor()
            query = 'CREATE SCHEMA IF NOT EXISTS {schema};'.format(schema=schema)
            cur.execute(query)

    def load_table(self, table_name, schema):
        """Reads Table and stores in a Pandas Dataframe"""
        with self.engine.begin() as conn:
            df = pd.read_sql_table(table_name=table_name, con=conn, schema=schema)
            return df

    def load_query_table(self, query):
        """Reads a SQL Query and stores in a Pandas Dataframe"""
        with self.engine.begin() as conn:
            df = pd.read_sql(query, conn)
            return df

    def write_query_table(self, query):
        """Given a Create Table Query. Execute the Query to write against the DWH"""
        conn_string = "host={0} user={1} dbname={2} password={3}".format(
            self.host, self.user, self.dbname, self.password)
        conn = ps.connect(conn_string)
        with conn:
            cur = conn.cursor()
            cur.execute(query)

    def write_df_table(self, df, table_name, schema, dtype=None, if_exists='replace', index=False):
        """Writes Pandas Dataframe to Table in DB"""
        self.create_schema(schema=schema)

        with self.engine.begin() as conn:
            df_to_sql(db_conn=conn,
                      df=df,
                      table_name=table_name,
                      schema=schema,
                      required_type_map=dtype,
                      if_exists=if_exists,
                      use_index=index,
                      chunksize=None)
