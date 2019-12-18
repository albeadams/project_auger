import cx_Oracle as oracle
import pandas as pd
import sys
import config

class IngestData(object):

  def __init__(self):
    pass

  
  def connect(self, username, password, client):
    self.connection = oracle.connect(username, password, client)
  

  def close(self):
    self.connection.close()


  def exec_query(self, query):
    cursor = self.connection.cursor()
    cursor.execute(query)
    df = pd.DataFrame(cursor)
    cursor.close()
    return df



