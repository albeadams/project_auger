

class RunAuger(object):

  def __init__(self, dataset=None, learners=None):
    self.dataset = dataset
    self.learners = learners

  def stage(self):
    print("this is the staging area")