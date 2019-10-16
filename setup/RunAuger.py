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
        processes can be created in order (pre-process, run through learners, test, etc.)
    '''
    process = procdata.ProcessData()
    process.prep_training_data(self.dm)

    #HERE

