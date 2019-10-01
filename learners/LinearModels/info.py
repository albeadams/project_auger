#### LinearRegression ####

linparams = """\n
  Params:
    1. fit_intercept :: True uses best fit line, False forces line to cross (0,0)
    2. normalize :: if fit_intercept=False, ignore
      else if normalize=True, normalize data
        (why normalize?
          a. reduce to scale for intpretation
          b. so large numbers don't overwhelm small
          c. enhances gradient descent
          (use StandardScalar to standardize before fit))
    3. copy_x :: True makes a copy of X dimensions, else they could be overwritten
    4. n_jobs :: number of jobs for compute,
        only matters if there are more than 1 target;
        -1 uses all processors\n"""

linresult = """\n
  Result: 
    coef_ :: estimated coefficients, either a 1D array for single target
        or 2D array for multiple targets;
        the values X's are multipled by to obtained y,
        i.e. the linear equation  
    intercept_ :: independent term (the y-intercept)\n"""

linexample = """\n
  Example:
    import numpy as np
    from sklearn.linear_model import LinearRegression
    X = np.array([[1,1], [1,2], [2,2], [2,3]])
    y = np.dot(X, np.array([1,2])) + 3  // for some random results
    reg = LinearRegression().fit(X, y)
    reg.score(X,y) // 1.0
    reg.coef_ // array([1., 2.])
    reg.intercept_ //3.0000
    reg.predict(np.array([[3, 5]])) // array([16.])\n"""

linmethods = """\n
  Methods:
    fit(X, y, sample_weight) :: fit linear model  
    get_params() :: returns parameters, i.e. fit_interecept, copy_x, etc.
    predict(X) :: input new values to get predicted result
    score(X, y, sample_weight) :: returns coefficient of determination R^2 if prediction
      - measures accuracy; R^2 = 1 - (RSS/TSS)
      - RSS = Residual sum of squares - variability left unexplained after regression
      - TSS = total variance in y
      - R^2 is proportion of variability in y that is explained by X using our model
      - http://benalexkeen.com/linear-regression-in-python-using-scikit-learn/ (also has mean squared error)
    set_params(...) :: sets parameters, see documentation\n"""

linnotes = """\n
  Notes:
    LinearRegression, aka Ordinary Least Squares,
    finds the coefficients for a data set as straight line.
    I.e. it finds one set of betas. It does not consider
    which variables are more important. This makes it heavily biased.
    A curved line that touched each data point would have little bias,
    but would suffer from overfitting (i.e. not generalizing).
    Curved line has low bias, but high variability, i.e. 
    it gives different results when tested against data 
    outside training set. Might do well sometimes, others terribly.
    Straight line has high bias, but low variance, sums of squares
    similar for different data sets. Straight line gives good,
    but not great predicitons, but consistently good. Ideal
    of ML is to have low bias and low variance.\n"""




#### RidgeRegression ####

rdgparams = """\n
  Params:
    1. alpha :: regularization strength, must be positive;
      reduces variance of estimates, where larger values are stronger regularization
      (can be an array of alphas, but number must correspond to number of targets)
    2. fit_intercept :: True uses best fit line, False forces line to cross (0,0)
    2. normalize :: if fit_intercept=False, ignore
      else if normalize=True, normalize data
        (why normalize?
          a. reduce to scale for intpretation
          b. so large numbers don't overwhelm small
          c. enhances gradient descent
          (use StandardScalar to standardize before fit))
    3. copy_x :: True makes a copy of X dimensions, else they could be overwritten
    4. max_iter :: max number of iterations for gradient solver;
      for sparse_cg and lsqr solvers, determined by scipy; for sag, default is 1000
    5. tol :: precision of solution
    6. solver :: {'auto','svd','cholesky','lsqr','sparse_cg','sag','saga'}
      Solver to use in computation:
        auto = choose solver automatically based on data type
        svd = use Singular Value Decomposition of X to computer coefficients;
          more stable than singular matrices than cholesky
        cholesky = use standard scipy.linalg.sovle function for closed-form solution
        sparse_cg = use conjugate gradient solver; iterative, so more appropriate
          than cholesky for large-scale data
        lsqr = uses dedicated regularized least-squares routine in scipy
          fastest and iterative
        sag = Stochastic Average Gradient descent, saga uses improved,
          unbiased version; both are iterative, faster than all others
          when n_samples and n_features are large
        [Note: all 5 support dense and sparse data, only sag and sprase_cg
          support sparse input with fit_intercept=True]
    7. random_state :: seed of random num generator\n"""

rdgresult = """\n
  Result: 
    coef_ :: weight vectors
    intercept_ :: independent term, set to 0.0 if fit_intercept=False
    n_iter :: number of iterations for each target; only used
      for sag and lsqr solvers\n"""

rdgexample = """\n
  Example:
    from sklearn.linear_model import Ridge
    import numpy as np
    n_samples, n_features = 10, 5
    rng = np.random.RandomState(0)
    y = rng.randn(n_samples)
    X = rng.random(n_samples, n_features)
    clf = Ridge(alpha=1.0)
    clf.fit(X,y)\n"""

rdgmethods = """\n
  Methods:
    fit(X, y, sample_weight) :: fit model
    get_params() :: get parametors
    predict(X) :: predict using model
    score(X, y, sample weight) :: return coefficient of determination R^2 of prediction;
      best score is 1.0
    set_params(**params) :: set parameters\n"""

rdgnotes = """\n
  Notes: Ridge uses least squares with L2 normalization. L2 differs from L1 in that
  L1 is the absolute deviation, whereas L2 is the squared deviation. Outliers with an error
  greater than 1 will be amplified using L2, and in minimizing the error, L2 will adjust
  more than L1, whereas L1 will ignore errors. The result is a linear model that is more stable.
  L1 norm can be useful as it comes with built-in feature selection, i.e. it can produce
  zero-value coefficients which allow the model to hone in on the useful features. See notes.
  Ridge Regression useful if have a lot of parameters but very few data points. Why? 
  Using cross validation and Ridge penalty, smaller parameter values are preferred, reducing variance,
  making predictions less sensitive to training data.
  Ridge regression is sum of squared residuals + lambda * slope^2, (squaring slope is the L2 part)
  which is more bias, but less variance (worse fit on training data, but better longterm predictions).
  Lambda (upside down y) can be anything from 0 (which is just linear regression) to positive infinity
  and is determined using cross validation.
  Lambda is the alpha parameter in the scikit-learn model.\n"""


#### Lasso ####

lassoparams = """\n
  Params:
    1. alpha :: constant to multiply L1 term, default to 1.0, see notes on lambda.
      alpha = 0 is equivalent to least squares, so use LinearRegression instead.
    2. fit_intercept :: True uses best fit line, False forces line to cross (0,0)
    3. normalize :: if fit_intercept=False, ignore
      else if normalize=True, normalize data
        (why normalize?
          a. reduce to scale for intpretation
          b. so large numbers don't overwhelm small
          c. enhances gradient descent
          (use StandardScalar to standardize before fit))
    4. precompute :: use precomputed Gram matrix to speed calculations (use auto)
    5. copy_x :: True makes a copy of X dimensions, else they could be overwritten
    6. max_iter :: max number of iterations for gradient solver
    7. tol :: tolerance of optimization
    8. warm_start :: if True, reuse solution of previous call
    9. positive :: if True, force coefficients to be positive
    10. random_state: pseudo random seed
    11. selection :: default is 'cyclic'; if 'random' is used, use random
      coefficient on each iteration rather than looping over features,
      for faster covergence (esp. when tol > 1e-4)\n"""

lassoresult = """\n
  Result: 
    coef_ :: weight vectors
    sparse_coef_ :: sparse representation of fitted coef_
    intercept_ :: independent term, set to 0.0 if fit_intercept=False
    n_iter :: number of iterations for each target\n"""

lassoexample = """\n
  Example:
    from sklearn import linear_model
    clf = linear_model.Lasso(alpha=0.1)
    clf.fit([[0,0],[1,1],[2,2]],[0,1,2])
    print(clf.coef_) # prints coefficients
    print(clf.intercept_) # prints 0.15\n"""

lassomethods = """\n
  Methods:
    fit(X, y, check_input) :: fit model with coordinate descent
      check_input = True alls to bypass input checking, don't use typically
    get_params() :: get parametors
    path(X, y, l1_ratio, eps, n_alphas, ...) :: compute elastic net path with coordinate descent
      - see ElasticNet for more info
    predict(X) :: predict using model
    score(X, y, sample weight) :: return coefficient of determination R^2 of prediction;
      best score is 1.0
    set_params(**params) :: set parameters\n"""

lassonotes = """\n
  Notes: Similar to Ridge. Used for sparse coefficients (see notes on L1 vs L2 norm). 
  Prefers non-zero coefficients, so can act effectively as feature selector.
  Instead of saying sum of squared residuals + lambda * slope^2, we have |slope|,
  this is Lasso Regression (L1). AS with Ridge, we have some bias to the fit line, but less variance.
  Similar to Ridge, make predictions less sensitive to training dataset.
  Both Ridge and Lasso shrink parameters but not equally.
  How differ? Ridge Regression can shrink the slope, as lambda increases (when 0, it's linear regression).
  But Ridge can only shrink slope asymptotically close to 0, while Lasso can shrink slope to 0.
  In other words, the larger we make lambda, the parameters of Ridge might shrink at different rates, but
  never get to 0, whereas Lasso can make the unimportant parameters shrink to 0, leaving only
  the important parameters for prediction. Can reduce variance in models that contain useless parameters,
  where Ridge is useful when parameters are all useful.
  Lambda (upside down y) can be anything from 0 (which is just linear regression) to positive infinity
  and is determined using cross validation.
  Lasso is technically the same as ElasticNet with ll_ratio=1.0 (no L2 penalty) according to scikit-learn.
  Lambda is the alpha parameter in the scikit-learn model.

  Lasso uses coordinate descent: considers each column of data at a time\n"""




#### ElasticNet ####

elasticparams = """\n
  Params:
    1. alpha :: constant to multiply the penalty terms, default to 1.0.
      alpha = 0 is equivalent to least squares, so use LinearRegression instead.
    2. l1_ratio :: mixing parameter, 0 <= l1_ratio <= 1; l1_ratio = 0 means
      the penalty is L2; l1_ratio = 1 is L1 penalty (Lasso); anywhere between 0 and 1,
      the penalty is combination of L1 and L2 penalty (0.5 is default)
    3. fit_intercept :: True uses best fit line, False forces line to cross (0,0)
    4. normalize :: if fit_intercept=False, ignore
      else if normalize=True, normalize data
        (why normalize?
          a. reduce to scale for intpretation
          b. so large numbers don't overwhelm small
          c. enhances gradient descent
          (use StandardScalar to standardize before fit))
    5. precompute :: use precomputed Gram matrix to speed calculations (use auto)
    6. max_iter :: max number of iterations for gradient solver
    7. copy_x :: True makes a copy of X dimensions, else they could be overwritten
    8. tol :: tolerance of optimization
    9. warm_start :: if True, reuse solution of previous call
    10. positive :: if True, force coefficients to be positive
    11. random_state: pseudo random seed
    12. selection :: default is 'cyclic'; if 'random' is used, use random
      coefficient on each iteration rather than looping over features,
      for faster covergence (esp. when tol > 1e-4)\n"""

elasticresult = """\n
  Result:
    coef_ :: weight vectors
    sparse_coef_ :: sparse representation of fitted coef_
    intercept_ :: independent term, set to 0.0 if fit_intercept=False
    n_iter :: number of iterations for each target\n"""

elasticexample = """\n
  Example:
    from sklearn.linear_model import ElasticNet
    from sklearn.datasets import make_regression
    X, y = make_regression(n_features=2, random_state=0)
    # note: make_regression generates a random regression problem
    regr = ElasticNet(random_state=0)
    regr.fit(X,y)\n"""

elasticmethods = """\n
  Methods:
    fit(X, y, check_input) :: fit model with coordinate descent
      check_input = True alls to bypass input checking, don't use typically
    get_params() :: get parametors
    path(X, y, l1_ratio, eps, n_alphas, ...) :: compute elastic net path with coordinate descent
      - see ElasticNet for more info
    predict(X) :: predict using model
    score(X, y, sample weight) :: return coefficient of determination R^2 of prediction;
      best score is 1.0
    set_params(**params) :: set parameters\n"""

elasticnotes = """\n
  Notes: Uses both L1 and L2 norm regularization. Can learn sparse model with few
  non-zero weights (Lasso) while maintaining regularization properties of Ridge.
  Control using l1_ratio parameter. Useful when multiple features are correlated.
  Lasso will pick one at random, elastic net will pick both. Inherits some of Ridge's stability.
  As with Ridge and Lasso, cross validation forms of this learner exist that can learn alpha and l1_ratio.
  Ridge is useful when we know all variables are useful, Lasso when we need help eliminating some.
  Elastic Net is when we don't know in advance if variables are useful or not useful.
  Starts with least squares, as Lasso and Ridge do. Then it combines the Lasso penalty
  with the Ridge penalty, but assigns weights to each (l1_ratio). Cross validation will
  give the best ratio.\n"""



#### BayesRegression ####

bayesparams = """\n
  Params:
    1. n_iter :: max number of iterations, default = 300
    2. tol :: stop if w has converged at this, default 0.001
    3. alpha_1 :: shape parameter for Gamma distribution over alpha parameter
    4. alpha_2 :: inver scale parameter for Gamma distribution prior over alpha parameter
    5. lambda_1 :: shape parameter for Gamma distribution over lambda parameter
    6. lambda_2 :: inverse scale parameter for Gamma distribution prior over lambda parameter
    7. compute_score :: compute log marginal likelihood at each iteration, default = False
    8. fit_intercept :: if False, data is considered centered, no intercept used
    9. normalize :: ignored if fit_intercept=False, else regressors normalized
      before regression by subtracting L2-norm
    10. copy_X :: True = create copy, else overwrite
    11. verbose :: verbosity\n"""

bayesresult = """\n
  Result:
    coef_ :: weight vectors
    intercept_ :: set to 0.0 if fit_intercept is False
    alpha_ :: estimated precision of noise
    lambda_ :: estimated precision of weights
    sigma_ :: estimated variance-covariance matrix of weights
    scores_ :: if compute_score=True, value is log marginal likelihood
      (to be maximized) at each iteration of optimization.
    n_iter :: number of iterations for each target\n"""

bayesexample = """\n
  Example:
    from sklearn import linear_model
    clf = linear_model.BayesianRidge()
    clf.fit([[0,0],[1,1],[2,2]], [0,1,2])
    clf.predict([[1,1]]) # returns 1\n"""

bayesmethods = """\n
  Methods:
    fit(X, y, sample_weight) :: fit model with coordinate descent
      check_input = True alls to bypass input checking, don't use typically
    get_params() :: get parametors
    predict(X, return_std) :: predict using model; return_std=True returns standard
      deviation of posterior prediction
    score(X, y, sample weight) :: return coefficient of determination R^2 of prediction;
      best score is 1.0
    set_params(**params) :: set parameters\n"""

bayesnotes = """\n
  A means of determining model complexity automatically while avoiding overfitting.
  A drawback is that this inference can be time consuming. In essence,
  Bayesian regression returns a probability distribution (Guassian), so not a single
  predictor but a posterior distribution for the model parameters. The basic formula is:
    Posterior = (Likelihood*Prior)/Normalization (see info.py in LinearModels for link).
    Priors would prior domain knowledge, or a guess on what model parameters should be.
    Without priors, can use non-informative priors, like normal distribution.
    The posterior prediction is based on the data and the priors. More and more
    data nullifies the prior, until the point (infinite data) when we essentially
    have a Linear Regression model. In practice, you approximate posterior by
    drawing samples from posterior. In other words, given a small data set,
    the Bayesian model will produce a range of outputs, whereas Ordinary Least Squares
    (Linear Regression), will have a single prediction. More data will converge this
    distribution to the OLS line because the priors are washed out by the likelihoods.
    The prediction from a Bayesian regression is also a range, with a peak value.
    Bayesian Regression is useful when we have limited data and prior knowledge of
    how the model works and shows the uncertainty inherent in this knowledge.
    From scikit-learn, note that Bayesian Regression more robust to ill-posed problems.\n"""


#### Logistic Regression ####

logparams = """\n
  Params:
    1. penalty :: 'l1', 'l2', 'elasticnet', 'none' (default is l2)
      the norm to use; newton-cg, sag and lbfgs solvers only support l2;
      elasticnet only supported by saga solver; none is no regularization
      (liblinear solver requires a penalty)
    2. dual :: dual or primal formulation; dual only for l2 wit liblinear;
      use dual=False with n_samples>n_features
    3. tol :: tolerance for stopping criteria
    4. C :: default=1.0; inverse of regularization strength, must be positive;
      smaller values mean stronger regularization
    5. fit_intercept :: if True, a constant added to decision fuction
    6. intercept_scaling :: if liblinear is used and fit_intercept=True;
      synthetic feature with constant value equal to intercept_scaling
      appended to instance vector; = intercept_scaling * synthetic_feature_weight;
      subject to l1/l2 regularization
    7. class_weight :: balanced, or a dictionary; balanced uses y to automatically
      adjust weights inversely proportional to class frequencies; none means all have one weight
    8. random_state :: seed of pseudo random state
    9. solver :: 'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'
      for small datasets: liblinear
      for larger datasets: sag, saga
      for multiclass problems: 'newton-cg', 'sag', 'saga', 'lbfgs' handle multinomial loss
        'liblinear' limited to one-versus-rest schemes
      L2 penalty: 'newton-cg', 'lbfgs', 'sag', 'saga'
      L1 penalty: 'liblinear', 'saga'
      elasticnet penalty: 'saga'
      Note: 'liblinear' must have a penalty
    10. max_iter :: default=100; max number of iterations
    11. multi_class :: 'ovr' (default), 'multinomial', 'auto';
      if 'ovr', binary problem fit for each label; 'multinomial' loss
      minimized is multinomial loss fit across entire probability distribution, 
      even with binary data (can't use with liblinear); 'auto' selects 'ovr' for
      binary data, or if solver='liblinear', otherwise selects 'multinomial'
    12. verboe :: for liblinear and lbfgs solvers, set to positive
    13. warm_start :: default=False; if true, reuse solution of previous call
      to fit as initialization
    14. n_jobs :: number of CPU cores used when parallelizing if multi-class='ovr';
      ignored if solver='liblinear'; None == 1
    15. l1_ratio :: elastic net mixing parameter 0 <= l1_ratio <= 1; only
      used if penalty='elasticnet'; 0 is equivalent to setting penalty='l2';
      1 is equivalent to penalty='l1'\n"""

logresult = """\n
  Result:
    classes_ :: list of class labels
    coef_ :: weight vectors (see documentation on multi_class='multinomial')
    intercept_ :: set to 0.0 if fit_intercept is False
    n_iter :: number of iterations for each target\n"""

logexample = """\n
  Example:
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
    clf.fit(X, y)
    clf.predict(X[:2, :]) #prints prediction
    clf.score(X, y) # prints score\n"""

logmethods = """\n
  Methods:
    decision_function(X) :: predict confidence score
    densify() :: convert coefficient matrix to dense array
    fit(X, y, sample_weight) :: fit model
    get_params() :: get parametors
    predict(X) :: predict using model
    predict_log_proba(X) :: log of probability estimates
    predict_proba(X) :: probability estimates
    score(X, y, sample weight) :: return mean accuracy of given test data
    set_params(**params) :: set parameters
    sparsify() :: convert coefficient matrix to sparse format; for
      L1 models, more memory and storage efficient (uses scipy.sparse);
      but for L2 without many zero coefficients, this would increase memory\n"""

lognotes = """\nTODO\n"""

### combo - done this way for sake of simplicity, allows for any single to be accessed via getters ###

linearinfo = linparams + linresult + linexample + linmethods + linnotes
ridgeinfo = rdgparams + rdgresult + rdgexample + rdgmethods + rdgnotes
lassoinfo = lassoparams + lassoresult + lassoexample + lassomethods + lassonotes
elasticinfo = elasticparams + elasticresult + elasticexample + elasticmethods + elasticnotes
bayesinfo = bayesparams + bayesresult + bayesexamples + bayesmethods + bayesnotes
loginfo = logparams + logresult + logexamples + logmethods + lognotes