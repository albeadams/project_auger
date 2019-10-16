import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

from sklearn.model_selection import train_test_split

from setup import DataMatrix as datamatrix
from setup import Input as inpt
from setup import info

class ProcessData(object):

  def __init__(self):
    pass


  def prep_training_data(self, dm=None):
    inp = inpt.Input()

    while True:
      hh = inp.get_input("Does your data have column headers? (y or n): ")
      if hh == 'y':
        dm.header = dm.df.columns.values
        break
      elif hh == 'n':
        break
      else:
        inp.print_out("Try again. Enter y for yes, n for no.")

    # split the dataframe in process, store it in datamatrxix
    dm.train_set, dm.test_set = self.easy_split(dm.df)
    dm.train_copy = dm.train_set.copy()

    # choose how to replace nan values
    if self.check_for_nulls(dm.train_copy):
      print(info.list_missing_values_options)
      while True:
        try:
          choice = inp.get_input("Your choice: ")
          if not (int(choice) > 13 or int(choice) < 1):
            break
          else:
            inp.print_out("Try again. ", end='')
        except ValueError:
          inp.print_out("Not a number, try again.")

      dm.choice = int(choice)
      # get the train set, pass it and choice to fix_nulls, which returns the fixed df
      # and the result of the computation, i.e. if max was the choice, the result would return
      # this numeric value; training=True created the replace_df and returns; training=False requires
      # the replace_df to be included in the call for certain choices, doesn't return a replace_df
      dm.train_copy, dm.replace_df  = self.fix_nulls(dm.train_copy, dm.choice, training=True)

      # checks if any columns not numeric, exit if so; will build in process options for this later
      if self.has_nonnumber_type(dm.train_copy):
        inp.print_out("Your data has non-numerical data.")
        inp.print_out("Please provide only numerical data.")
        exit()

    else:
      print(info.no_missing_found)
      dm.choice = 3 # default to 0 - TODO: should be able to specify

    #return dm


  # returns True if a column contains a non-numeric type
  def has_nonnumber_type(self, df=None):
    for col in df.columns:
      if not is_numeric_dtype(df[col]):
        return True
    return False


  # split data into training and testing
  def easy_split(self, df=None, test_size=0.2, random_state=42):
    return train_test_split(df, test_size=test_size, random_state=random_state)


  # return True if find nulls
  def check_for_nulls(self, df=None):
    if df.isnull().values.any():
      return True
    return False


  def fix_nulls(self, df=None, choice=1, training=True, replace_df=None):
    """
        gives options on how to fix nulls; default removes rows;
        if training=True, this is a test dataset, or new data;
        in that case, if using min, max, avg, median or most frequent,
        must pass those values using replace_df, a dataframe
        that should contain the replacement calculations for each column
        regardless of whether or not they were missing in training set;
        if choice=2 (remove column), replace_df must contain list of retained columns
        and any missing values in these remaining columns will be set to 0 (TODO give option)
    """

    if training == False and replace_df == None and (choice == 2 or (choice >= 4 and choice <= 8)):
      inp.print_out("You must supply a replacement dataframe to fix missing values.")
      return -1

    if choice == 1:
      # default is to drop rows; this helps if missing is non-numeric
      df.dropna(axis=0, inplace=True)
    elif choice == 2: # drop columns
      if training:
        df.dropna(axis=1, inplace=True)
        replace_df = df.columns.values
      else:
        df= df[replace_df] # remove columns from test set
        df.fillna(0, inplace=True) # default replace any nan left to 0
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