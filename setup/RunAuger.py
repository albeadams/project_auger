import learners
from setup import DataMatrix as datamatrix
from setup import ProcessData as procdata
from setup import Input as inp

class RunAuger(object):

  def __init__(self, directory=None, dataset=None, learner=None):
    self.directory = directory
    self.dataset = dataset
    self.learner = learner
    self.h = learners.Help()

    # DataMatrix will store headers if present;
    self.dm = datamatrix.DataMatrix(self.directory + self.dataset)
    while True:
      hh = inp.get_input("\n  Does your data have column headers? (y or n): ")
      if hh == 'y' or hh == 'n':
        if hh == 'y':
          self.dm.set_header()
        break
      else:
        print("\n  Try again. Enter y for yes, n for no.")


  ### represents programs 'main' after dataset and learner(s) chosen ###
  def stage(self):
    self.process = procdata.ProcessData(self.dm)

    # if dataset has ?, replace with np.nan
    self.process.replace_question_marks()

    # choose how to replace nan values
    if self.process.check_for_nulls():
      print("""\n  
  Your data has missing values.
  Here are your options on how to handle this:\n
      1. Remove offending row
      2. Remove offending column
      3. Replace missing values with... (to come) [min, max, avg,ffill, bfill]\n""")

      while True:
        choice = inp.get_input("  Your choice: ")
        if not (choice > 3 or choice < 1):
          break

      if choice == 3:
        print("""\n
  You chose to replace the missing values. There are several options:

    1. Replace with min
    2. Replace with max
    3. Replace with average
    4. Forward fill
    5. Backward fill
    6. Interpolate???

    [HERE - https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
      also note hands on... need to store whatever this is for use in test and later data...
      need to go back and split the data into test and train data before this, obtain 
      this fill value only from test]

          \n""")
      self.process.fix_nulls(choice)