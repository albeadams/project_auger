import pandas as pd
import sys

import Model
import IngestData
import config

class CreditRating(object):

  def __init__(self):
    pass

  def runmodel(self):
    ingdata = IngestData.IngestData()
    ingdata.connect(config.data['username'], config.data['password'], config.data['client'])

    try:
      df = ingdata.exec_query(config.q['rating'])
    except:
      print('query not found')
    finally:
      ingdata.close()

    m = Model.Model(df)
    m.process()


if __name__ == '__main__':
  CreditRating().runmodel()