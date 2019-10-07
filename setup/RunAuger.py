import learners
from setup import DataMatrix as datamatrix
from setup import ProcessData as procdata
from setup import Input as inp
from setup import info

class RunAuger(object):

  def __init__(self, directory=None, datafile=None, learner=None):
    self.directory = directory
    self.datafile = datafile
    self.learner = learner
    self.inp = inp.Input()
    self.process = procdata.ProcessData()
    self.dm = datamatrix.DataMatrix(directory, datafile)


  ### represents programs 'main' after dataset and learner(s) chosen ###
  def stage(self):

    # checks if any columns not numeric, exit if so
    if self.process.has_nonnumber_type(self.dm.df):
      self.inp.print_out("Your data has non-numerical data.")
      self.inp.print_out("Please provide only numerical data.")
      exit()

    while True:
      hh = self.inp.get_input("Does your data have column headers? (y or n): ")
      if hh == 'y':
        self.dm.header = self.dm.df.columns.values
        break
      elif hh == 'n':
        break
      else:
        self.inp.print_out("Try again. Enter y for yes, n for no.")

    # split the dataframe in process, store it in datamatrxix
    self.dm.train_set, self.dm.test_set = self.process.easy_split(self.dm.df)
    self.dm.train_copy = self.dm.train_set.copy()

    # choose how to replace nan values
    if self.process.check_for_nulls(self.dm.train_copy):
      print(info.list_missing_values_options)
      while True:
        try:
          choice = self.inp.get_input("Your choice: ")
          if not (int(choice) > 13 or int(choice) < 1):
            break
          else:
            self.inp.print_out("Try again. ", end='')
        except ValueError:
          self.inp.print_out("Not a number, try again.")

      self.dm.choice = choice

      # get the train set, pass it and choice to fix_nulls, which returns the fixed df
      # and the result of the computation, i.e. if max was the choice, the result would return
      # this numeric value; training=True created the replace_df and returns; training=False requires
      # the replace_df to be included in the call, doesn't return a replace_df
      res = self.dm.train_copy, self.dm.replace_df  = self.process.fix_nulls(self.dm.train_copy, self.dm.choice, training=True)
      if res == -1: 
        print("Error in fixing training nulls")
        exit() # shouldn't occur
    else:
      print(info.no_missing_found)
      self.dm.choice = 3 # all future set to 0 - change: should be able to specify

    # HERE

