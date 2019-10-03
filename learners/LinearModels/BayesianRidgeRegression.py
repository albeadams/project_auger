from sklearn import linear_model

class BayesianRidgeRegression(object):

  def __init__(self,
    n_iter=300,
    tol=0.001,
    alpha_1=1e-06,
    alpha_2=1e-06,
    lambda_1=1e-06,
    lambda_2=1e-06,
    compute_score=False,
    fit_intercept=True,
    normalize=False,
    copy_X=True,
    verbose=False):

    self.learner = linear_model.BayesRidge(
      n_iter=n_iter,
      tol=tol,
      alpha_1=alpha_1,
      alpha_2=alpha_2,
      lambda_1=lambda_1,
      lambda_2=lambda_2,
      compute_score=compute_score,
      fit_intercept=fit_intercept,
      normalize=normalize,
      copy_X=copy_X,
      verbose=verbose)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.bayesinfo