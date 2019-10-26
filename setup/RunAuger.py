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
    
    self.dm = datamatrix.DataMatrix(directory, datafile)


  def stage(self):
    '''
        represents programs 'main' after dataset and learner(s) chosen;
        ProcessData requires a DataMatrix
    '''
    inp = inpt.Input()
    process = procdata.ProcessData(self.dm)

    while True:
      hh = inp.get_input("Does your data have column headers? (y or n): ")
      if hh != 'y' && hh != 'n':
        inp.print_out("Try again. Enter y for yes, n for no.")
      else:
        if hh == 'y':
          self.dm.header = self.dm.df.columns.values
        break
        
    #default is train_test_split, 0.2 test, 42 random
    self.dm.train_set, self.dm.test_set = process.split_data(self.dm.df, type='train_test_split')
    self.dm.train_copy = self.dm.train_set.copy()

    if process.check_for_nulls(self.dm.df):
      print(info.list_missing_values_options)
      while True:
        try:
          choice = inp.get_input("Your choice: ")
          if not (int(choice) > 13 or int(choice) < 1):
            break
          inp.print_out("Try again. ", end='')
        except ValueError:
          inp.print_out("Not a number, try again.")
      self.dm.choice = int(choice)
      self.dm.train_copy, self.dm.replace_df = process.fix_nulls(df=self.dm.df, choice=int(choice), training=True)
    else:
      print(info.no_missing_found)
      self.dm.choice = 3 # default to 0 - TODO: should be able to specify


    process.create_bins(self.dm.df) # if non-numeric data found



    #HERE

