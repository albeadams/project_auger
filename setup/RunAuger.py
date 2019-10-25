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
    process = procdata.ProcessData(self.dm)
    process.get_headers(self.dm.df)
    process.split_data(self.dm.df) #default is train_test_split, 0.2 test, 42 random
    process.replace_nan(self.dm.df)
    process.create_bins(self.dm.df) # if non-numeric data found



    #HERE

