import pandas as pd
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=157.230.40.120;'
                      'Database=master;'
                      'UID=sa;'
                      'PWD=123456Aa;'
                      'Trusted_Connection=no;')
cursor = conn.cursor()


def execute_query(query):
    cursor.execute(query)
    conn.commit()


def read_sql_query(query):
    return pd.read_sql_query(query, conn)
