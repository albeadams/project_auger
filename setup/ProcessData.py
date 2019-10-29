import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

from sklearn.model_selection import train_test_split

from setup import DataMatrix as datamatrix

class ProcessData(object):

  def __init__(self, dm):
    pass


  def split_data(self, df=None, type='train_test_split', test_size=0.2, random_state=42):
    # split the dataframe in process, store it in datamatrxix
    if type == 'train_test_split':
      X = df.iloc[:,:-1]
      y = df.iloc[:,-1]
      return train_test_split(X, y, test_size=test_size, random_state=random_state)
    else:
      inp.print_out("Split type not supported")
      exit()


  # returns True if a column contains a non-numeric type
  def has_nonnumber_type(self, df=None):
    for col in df.columns:
      if not is_numeric_dtype(df[col]):
        return True
    return False


  # return True if find nulls
  def check_for_nulls(self, df=None):
    if df.isnull().values.any():
      return True
    return False


  def fix_nulls(self, df=None, choice=1, training=True, replace_df=None):
    """
        gives options on how to fix nulls; default removes rows;
        if training=False, this is a test dataset, or new data;
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


  def show_sample(self, df=None):
    # FIX: should print number, column name, maybe small sample horizontally
    inp.print_out(df.head())


  def create_bins(self, df=None, col=None):
    '''
      offers binning options; or drop column;
      if drop, should reset columns in self.dm.df and replace_df
    '''
    if not has_nonnumber_type(df):
      inp. #TODO: fix, this function offers binning options and the bins
      # or another function offer binning options and then calls this function
    nonint_found = [type(col) for col in df]
    for index, column in enumerate(nonint_found):
      inp.print_out('found non-integer at column ')
      # could use built in funciton has_nonnumber_type?
      
      #note: should also be able to manual specificy what columns to bin (i.e. is integer, but want to bin it)

