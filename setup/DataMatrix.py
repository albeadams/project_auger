import pandas as pd
import numpy as np

class DataMatrix(object):

  def __init__(self, directory=None, datafile=None):
    self.directory = directory
    self.datafile = datafile
    self.df = pd.read_csv(directory+datafile, sep=',', na_values=['?'])
    self.header = None
    self.train_set = None
    self.test_set = None
    self.train_copy = None
    self.choice = None
    self.replace_df = None # missing values

  def get_numpy_array(self):
    return self.df.to_numpy()