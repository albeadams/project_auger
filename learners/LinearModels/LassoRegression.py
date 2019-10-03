from sklearn import linear_model

class LassoRegression(object):

  def __init__(self,
    alpha=1.0,
    fit_intercept=True,
    normalize=False,
    precompute=False,
    copy_X=True,
    max_iter=1000,
    tol=0.0001,
    warm_start=False,
    positive=False,
    random_state=None,
    selection='cyclic'):

    self.learner = linear_model.Lasso(
      alpha=alpha,
      fit_intercept=fit_intercept,
      normalize=normalize,
      precompute=precompute,
      copy_X=copy_X,
      max_iter=max_iter,
      tol=tol,
      warm_start=warm_start,
      positive=positive,
      random_state=random_state,
      selection=selection)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.lassoinfo