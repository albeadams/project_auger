import learners
from setup import DataMatrix as datamatrix
from setup import ProcessData as procdata
from setup import Input as inp
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

    if inp.get_input(str='Does your data have column headers? (y or n): ',
                      yn=True, errormsg=ERRORMSG_YN) == 'y':
        self.dm.header = self.dm.df.columns.values
        
    #default is train_test_split, 0.2 test, 42 random
    self.dm.train_set, self.dm.test_set = process.split_data(self.dm.df, type='train_test_split')
    self.dm.train_copy = self.dm.train_set.copy()
    local_df = self.dm.train_copy

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
      choice = inp.get_input('Select columns')  # need to provide numbered list of columns with sample
      # will also automaticlaly force binning of non-integercolumns.. create_bins returns list of non-integer...?
      column_choices = pick_columns(local_df)
      process.create_bins(local_df) # if non-numeric data found



    #HERE
    self.dm.train_copy = local_df
