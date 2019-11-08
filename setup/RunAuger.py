import learners
from setup import DataMatrix as datamatrix
from setup import ProcessData as procdata
from setup import Input as inpt
from setup import info

ERRORMSG_YN = 'Try again. Enter y for yes, n for no.'

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

    if inp.get_input(strn='Does your data have column headers? (y or n): ',
                      yn=True, errormsg=ERRORMSG_YN) == 'y':
        self.dm.header = self.dm.df.columns.values
        
    #default is train_test_split, 0.2 test, 42 random
    self.dm.X_train, self.dm.X_test, self.dm.y_train, self.dm.y_test = process.split_data(self.dm.df, type='train_test_split')
    self.dm.X_train_copy = self.dm.X_train.copy()
    local_df = self.dm.X_train_copy

    if process.check_for_nulls(local_df):
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
      local_df, self.dm.replace_df = process.fix_nulls(df=local_df, choice=int(choice), training=True)
    else:
      print(info.no_missing_found)
      self.dm.choice = 3 # default to 0 - TODO: should be able to specify

    to_bin = 'y'
    if not process.has_nonnumber_type(local_df):
      inp.print_out('No non-integer columns found.')
      to_bin = inp.get_input('Do you still need to bin any columns? (y or n): ',
                            yn=True, errormsg=ERRORMSG_YN)
    
    if to_bin == 'y':
      process.show_sample(local_df)
      while True:
        column_choice = inp.get_input('Select column (one at a time, "done" when complete, "auto" to automate)')
        if column_choice == 'done':
          if process.has_nonnumber_type(local_df):
            inp.print_out('You still have non-number columns, please select those, or type "auto"')
          else:
            break
        elif column_choice == 'auto':
          process.create_bins(local_df, method='auto')
          break
        else:
          try:
            col = int(column_choice)
            if col < 1 or col > len(local_df.columns):
              inp.print_out('Number should be between 1 and max column ' + str(len(local_df.columns)))
            else:
              process.create_bins(local_df, col=col)
          except ValueError:
            inp.print_out('Not a column number, should be between 1 and max column ' + str(len(local_df.columns)))


    #normalize options...

    #at end, set X_train_copy
    self.dm.X_train_copy = local_df
