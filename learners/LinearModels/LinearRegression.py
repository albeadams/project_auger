import info

from sklearn import linear_model

class LinearRegression(object):

  def __init__(self,
    fit_intercept=True,
    normalize=False,
    copy_X=True,
    n_jobs=None):

    self.learner = linear_model.LinearRegression(
      fit_intercept=fit_intercept,
      normalize=normalize,
      copy_X=copy_X,
      n_jobs=n_jobs)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.linearinfo