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
          if not (int(choice) > 3 or int(choice) < 1):
            break
          else:
            self.inp.print_out("Try again. ", end='')
        except ValueError:
          self.inp.print_out("Not a number, try again.")


      # get the train set, pass it and choice to fix_nulls, which returns the fixed df
      # and the result of the computation, i.e. if max was the choice, the result would return
      # this numeric value
      while True:
        self.dm.train_copy, replace_df  = self.process.fix_training_nulls(self.dm.train_copy, choice)
        if not result == -1:
          break

      self.dm.store_missing_value(replace_df, choice) # for future test set and other data, replace missing data
        # NOTE: need to add new method to ProcessDAta that takes in the replace df and choice...
    else:
      print(info.nomissingfound)
      #self.dm.store_missing_value(self.dm.train_copy, 0) # correct format for result?


