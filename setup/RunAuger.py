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


  ### represents programs 'main' after dataset and learner(s) chosen ###
  def stage(self):

    process = procdata.ProcessData()
    self.dm = process.prep_training_data(self.dm)


