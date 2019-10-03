import learners
from setup import DataMatrix as datamatrix
from setup import ProcessData as procdata
from setup import Input as inp
from setup import info

class RunAuger(object):

  def __init__(self, directory=None, dataset=None, learner=None):
    self.directory = directory
    self.dataset = dataset
    self.learner = learner
    self.inp = inp.Input()
    self.process = procdata.ProcessData()
    # DataMatrix will store headers if present;
    self.dm = datamatrix.DataMatrix(self.directory + self.dataset)
    while True:
      hh = self.inp.get_input("\n  Does your data have column headers? (y or n): ")
      if hh == 'y' or hh == 'n':
        if hh == 'y':
          self.dm.set_header()
        break
      else:
        print("\n  Try again. Enter y for yes, n for no.")



  ### represents programs 'main' after dataset and learner(s) chosen ###
  def stage(self):
    # split the dataframe in process, store it in datamatrxix
    train_set, test_set = self.process.easy_split(self.dm.get_dataframe())
    self.dm.store_train_test_data(train_set, test_set)

    # choose how to replace nan values
    if self.process.check_for_nulls(self.dm.get_train_set()):
      print(info.missingvalues)
      while True:
        choice = self.inp.get_input("  Your choice: ")
        if not (choice > 3 or choice < 1):
          break

      if choice == 3:
        print(info.replacewithoptions)

      # get the train set, pass it and choice to fix_nulls, which returns the fixed df
      # and the result of the computation, i.e. if max was the choice, the result would return
      # this numeric value
      self.dm.store_missing_value(self.process.fix_nulls(self.dm.get_train_set(), choice), result)
    else:
      print(info.nomissingfound)
      self.dm.store_missing_value(self.dm.get_train_set(), 0) # correct format for result?


