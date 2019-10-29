import pandas as pd
import numpy as np

class DataMatrix(object):

  def __init__(self, directory=None, datafile=None, na_values='?'):
    self.directory = directory
    self.datafile = datafile
    self.df = pd.read_csv(directory+datafile, sep=',', na_values=na_values)
    self.header = None
    self.X_train = None
    self.X_test = None
    self.y_train = None
    self.y_test = None
    self.X_train_copy = None
    self.choice = None
    self.replace_df = None # missing values

  def get_numpy_array(self):
    return self.df.to_numpy()