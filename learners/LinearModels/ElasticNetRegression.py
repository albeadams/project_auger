from sklearn import linear_model

class ElasticNetRegression(object):

  def __init__(self,
    alpha=1.0,
    l1_ratio=0.5,
    fit_intercept=True,
    normalize=False,
    precompute=False,
    max_iter=1000,
    copy_X=True,
    tol=0.0001,
    warm_start=False,
    positive=False,
    random_state=None,
    selection='cyclic'):

    self.learner = linear_model.ElasticNet(
      alpha=alpha,
      fit_intercept=fit_intercept,
      normalize=normalize,
      precompute=precompute,
      max_iter=max_iter,
      copy_X=copy_X,
      tol=tol,
      warm_start=warm_start,
      positive=positive,
      random_state=random_state,
      selection=selection)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.elasticinfo