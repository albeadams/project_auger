import info

from sklearn import linear_model

class RidgeRegression(object):

  def __init__(self,
    alpha=1.0,
    fit_intercept=True,
    normalize=False,
    copy_X=True,
    max_iter=None,
    tol=0.001,
    solver='auto',
    random_state=None):

    self.learner = linear_model.Ridge(
      alpha=alpha,
      fit_intercept=fit_intercept,
      normalize=normalize,
      copy_X=copy_X,
      max_iter=max_iter,
      tol=tol,
      solver=solver,
      random_state=random_state)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.ridgeinfo