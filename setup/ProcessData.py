import pandas as pd
import numpy as np

from setup import DataMatrix as datamatrix

class ProcessData(object):

  def __init__(self, dm=None):
    self.dm = dm
    self.df = None


  # common to replace missing values with ? in dataset, this replaces them with np.nan
  def replace_question_marks(self):
      df = self.dm.get_dataframe()
      df.replace('?', np.nan, inplace=True)
      self.dm.set_dataframe(df)


  # return True if find nulls
  def check_for_nulls(self):
    if self.dm.get_dataframe().isnull().values.any():
      return True
    return False


  # gives options on how to fix nulls; default removes rows
  def fix_nulls(self, choice=1):
    self.df = self.dm.get_dataframe()
    if choice == 1:
      # drops all rows with any np.nan, no matter column
      self.df = self.df.dropna()
    elif choice == 2:
      # https://stackoverflow.com/questions/36226083/how-to-find-which-columns-contain-any-nan-value-in-pandas-dataframe-python
      self.df = self.df.drop(self.df.loc[:, self.df.columns[self.df.insa().any()].tolist()], axis=1)
    else:
      print("HERE - give options on zero, mean, median... ")
    self.dm.set_dataframe(self.df)