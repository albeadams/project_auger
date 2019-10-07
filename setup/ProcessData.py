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
  def fix_nulls(self, df=None, choice=1, training=True, replace_df=None):

    if training == False and replace_df == None and (choice >= 4 and choice <= 8):
      print("You must supply a replacement dataframe to fixing missing values.")
      return -1
    elif training == True and not replace_df == None:
      print("You must set training=False if supplying a replacement dataframe")
      return -1

    if choice == 1:
      # default is to drop rows; this helps if missing is non-numeric
      df.dropna(axis=0, inplace=True)
    elif choice == 2: # drop columns
      df.dropna(axis=1, inplace=True)
    elif choice == 3: # fill with 0
      df.fillna(0, inplace=True)
    elif choice == 4:
      if training:
        replace_df = df.min()
      df.fillna(replace_df, inplace=True)
    elif choice == 5:
      if training:
        replace_df = df.max()
      df.fillna(replace_df, inplace=True)
    elif choice == 6:
      if training:
        replace_df = df.mean()
      df.fillna(replace_df, inplace=True)
    elif choice == 7:
      if training:
        replace_df = df.median()
      df.fillna(replace_df, inplace=True)
    elif choice == 8:
      if training:
        replace_df = df.mode()
      df.fillna(replace_df, inplace=True)
    elif choice == 9:
      df.ffill(axis=0, inplace=True)
      # filling along column not supported
    elif choice == 10:
      df.bfill(axis=0, inplace=True)
    elif choice == 11:
      df.ffill(axis=0, inplace=True).bfill(axis=0, inplace=True)
    elif choice == 12:
      df.interpolate(method='linear', inplace=True)
    elif choice == 13:
      df.interpolate(method='index', inplace=True)

    if training:
      return df, replace_df
    else:
      return df