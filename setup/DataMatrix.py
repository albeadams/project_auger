import pandas as pd
import numpy as np

class DataMatrix(object):

  def __init__(self, datafile=None):
    self.df = pd.read_csv(datafile, sep=',')
    self.header = None

  def get_dataframe(self):
    return self.df

  def get_numpy_array(self):
    return self.df.to_numpy()

  def get_header(self):
    return self.header

  def set_dataframe(self, df):
    self.df = df

  def set_header(self):
    self.header = self.df.columns.values