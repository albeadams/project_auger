import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from setup import DataMatrix as datamatrix

class ProcessData(object):

  def __init__(self):
    pass

  # split data into training and testing
  def easy_split(self, df=None, test_size=0.2, random_state=42):
    return train_test_split(df, test_size=test_size, random_state=random_state)


  # return True if find nulls
  def check_for_nulls(self, df=None):
    if df.isnull().values.any():
      return True
    return False


  # gives options on how to fix nulls; default removes rows
  def fix_nulls(self, df=None, choice=1):
    if choice == 1:
      # drops all rows with any np.nan, no matter column
      df = df.dropna()
    elif choice == 2:
      # https://stackoverflow.com/questions/36226083/how-to-find-which-columns-contain-any-nan-value-in-pandas-dataframe-python
      df = df.drop(df.loc[:, df.columns[df.insa().any()].tolist()], axis=1)
    else:
      print("HERE - give options on zero, mean, median... ")
 
    result = None # this will store the result of any computation, i.e. max, zero, etc.

    return df, result

    ### note, no matter the choice, it must be stored in the DataMatrix object
    ### so that test set, and future data, can access this if they have missing data