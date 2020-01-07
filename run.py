import pandas as pd
import sys

import config
import IngestData
import Model as md


def main(args):
  ingdata = IngestData.IngestData()
  ingdata.connect(config.data['username'], config.data['password'], config.data['client'])

  datasets = {}

  try:
    # can return multiple datasets
    for idx, arg in enumerate(args):
      datasets[args[idx]] = ingdata.exec_query(config.q[args[idx]])
  except:
    print('query not found')
  finally:
    ingdata.close()



  #md.Model(df).run()

if __name__ == '__main__':
  main(sys.argv[1:])