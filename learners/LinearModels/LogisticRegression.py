import info

from sklearn import linear_model

class LogisticRegression(object):

  def __init__(self,
    penalty='l2',
    dual=False,
    tol=0.0001,
    C=1.0,
    fit_intercept=True,
    intercept_scaling=1,
    class_weight=None,
    random_state=None,
    solver='warn',
    max_iter=100,
    multi_class='warn',
    verbose=0,
    warm_start=False,
    n_jobs=None,
    l1_ratio=None)

    self.learner = linear_model.LogisticRegression(
      penalty='l2',
      dual=dual,
      tol=tol,
      C=1.0,
      fit_intercept=fit_intercept,
      intercept_scaling=intercept_scaling,
      class_weight=class_weight,
      random_state=random_state,
      solver=solver,
      max_iter=max_iter,
      multi_class=multi_class,
      verbose=verbose,
      warm_start=warm_start,
      n_jobs=n_jobs,
      l1_ratio=l1_ratio)

  def getlearner(self):
    return self.learner

  def help(self):
    return info.loginfo