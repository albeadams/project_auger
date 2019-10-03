import pandas as pd
import numpy as np

class DataMatrix(object):

  def __init__(self, datafile=None):
    self.df = pd.read_csv(datafile, sep=',', na_values=['?'])
    self.header = None

  def store_train_test_data(self, train_set=None, test_set=None):
    self.train_set = train_set
    self.test_set = test_set
    self.train_set_copy = self.train_set.copy()

  def store_missing_values(self, df=None, choice=None):
    pass

  # getters and setters
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

  # important to note - this returns copy of training set
  def get_train_set(self):
    return self.train_set_copy

  # this updates the copy of the training set
  def set_train_set(self, df=None):
    self.train_set_copy = df