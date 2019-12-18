import DT

class Model(object):

  def __init__(self, df):
    self.df = df
    print('Data to model:\n')
    print(self.df)
    print()


  def run(self):
    print('here')