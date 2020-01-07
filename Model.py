import numpy as np
import pandas as pd
from collections import defaultdict
import random

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

import DT
import ReplaceMissingTransformer

SEED = random.seed(42)

class Model(object):

  def __init__(self, df):
    self.df = df

  def process(self):
    imp = SimpleImputer(missing_values=np.nan, strategy='constant')
    df_repl = imp.fit_transform(self.df)
    df_zeros = np.where(df_repl != 'missing_value', df_repl, 0.0)

    df = pd.DataFrame(data=df_zeros)
    d = defaultdict(LabelEncoder)
    fit = df.apply(lambda x: d[x.name].fit_transform(x))

    self.df = fit

  def fit(self):
    X = self.df.iloc[:10000,:-1]
    y = self.df.iloc[:10000,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=SEED)
    clf = DecisionTreeClassifier(random_state=42, max_depth=3)
    print('performing cross val')
    print(cross_val_score(clf, X, y, cv=10))